import unittest
from unittest.mock import MagicMock
from bbscript import Runtime
from bbscript.constants import CMD_ARRAY
from bbscript.errors import SyntaxError
from bbscript.flags import StopExecutionNoRecover, RepeatStatement

class TestRuntime(unittest.TestCase):

	def test_load_script_ctx_constructor(self):
		script = ["test"]
		ctx = {"test": True}
		rt = Runtime(ctx, script)

		self.assertEqual(rt.script[0], script[0])
		self.assertNotEqual(rt.ctx, ctx)
		self.assertEqual(rt.ctx.get("test"), ctx.get("test"))
	
	def test_load_script(self):
		script = ["test"]
		rt = Runtime()
		rt.load_script(script)

		self.assertEqual(rt.script[0], script[0])

	def test_load_ctx(self):
		ctx = {"test": True}
		rt = Runtime()
		rt.update_context(ctx)

		self.assertNotEqual(rt.ctx, ctx)
		self.assertEqual(rt.ctx.get("test"), ctx.get("test"))

	def test_list_functions(self):
		rt = Runtime()
		for fn in rt.list_functions():
			self.assertTrue(fn in rt.ctx.keys())

	def test_list_variables(self):
		rt = Runtime()
		rt.ctx.update({
			"$test": "i am var"
		})
		for var in rt.list_variables():
			self.assertTrue("$%s" % var in rt.ctx.keys())

		self.assertEqual(rt.ctx.get("$test"), "i am var")
	
	def test_function_call(self):
		ctx = {
			"TEST": MagicMock(name="Custom Function TEST")
		}
		script = [
			["TEST", "arg1"]
		]
		rt = Runtime(ctx, script)

		for l in rt.exec():
			pass

		rt.ctx.get("TEST").assert_called_with(rt.ctx, "arg1")

	def test_resolve_arg_array(self):
		rt = Runtime()
		result = rt.resolve_argument([CMD_ARRAY, 1, 2, 3])
		self.assertEqual(result, [1, 2, 3])

	def test_resolve_arg_block(self):
		rt = Runtime()
		result = rt.resolve_argument([["FN1", "FN2"]])
		self.assertEqual(result, [["FN1", "FN2"]])

	def test_resolve_arg_statement(self):
		rt = Runtime()
		rt.update_context({
			"TEST": MagicMock(name="TEST", side_effect=lambda ctx: "test_result")
		})		
		result = rt.resolve_argument(["TEST"])
		rt.ctx.get("TEST").assert_called_with(rt.ctx)
		self.assertEqual(result, "test_result")

	def test_early_exit(self):
		ctx = {
			"FN1": MagicMock(name="FN1"),
			"FN2": MagicMock(name="FN2", return_value=StopExecutionNoRecover()),
			"FN3": MagicMock(name="FN3")
		}
		script = [
			["FN1"],
			["FN2"],
			["FN3"]
		]
		rt = Runtime(ctx, script)

		for l in rt.exec():
			pass

		rt.ctx.get("FN1").assert_called()
		rt.ctx.get("FN2").assert_called()
		rt.ctx.get("FN3").assert_not_called()

	def test_single_line(self):
		ctx = {
			"TEST": MagicMock(name="Custom Function TEST", return_value=123)
		}
		script = [
			["TEST", "arg1"]
		]
		rt = Runtime(ctx)

		result = rt.exec_line(["TEST", "arg1"])

		self.assertEqual(result, 123)
		rt.ctx.get("TEST").assert_called_with(rt.ctx, "arg1")

	def test_break_on_non_arrays(self):
		rt = Runtime()
		self.assertRaises(SyntaxError, lambda: rt.exec_line("TEST"))

	def test_repeat_statement(self):
		def testMock(ctx):
			ctx["$counter"] = ctx["$counter"] + 1
			return RepeatStatement() if ctx["$counter"] < 2 else None

		ctx = {
			"$counter": 0,
			"TEST": MagicMock(name="Custom Function TEST", side_effect=testMock)
		}
		script = [
			["TEST"]
		]
		rt = Runtime(ctx, script)
		for l in rt.exec():
			pass

		self.assertEqual(rt.ctx.get("TEST").call_count, 2)

	def test_block_insertion(self):

		ctx = {
			"TEST": MagicMock(name="TEST", return_value=[["FN1"], ["FN2"]])
		}
		rt = Runtime(ctx)
		rt.exec_line(["TEST", "arg1"])
		self.assertEqual(rt.script, [["FN1"], ["FN2"]])

	def test_resolve_block(self):
		rt = Runtime()
		rt.exec_line([["TEST", "arg1"]])
		self.assertEqual(rt.script, [["TEST", "arg1"]])

	def test_call_unsupported_function(self):
		rt = Runtime()
		result = rt.exec_line(["TEST"])

		self.assertTrue(isinstance(result, StopExecutionNoRecover))
		self.assertEqual(rt.ctx.get("$error"), "Unsupported command: TEST")
