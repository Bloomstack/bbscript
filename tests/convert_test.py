import unittest
from bbscript.stdlib.convertions import cmd_int, cmd_float, cmd_string, cmd_bool, cmd_undefined

class TestConvert(unittest.TestCase):
	def test_int(self):
		self.assertTrue(isinstance(cmd_int({}, 1.0), int))
		self.assertTrue(isinstance(cmd_int({}, "1.0"), int))
		self.assertTrue(isinstance(cmd_int({}, "abc"), int))

	def test_float(self):
		self.assertTrue(isinstance(cmd_float({}, 1), float))
		self.assertTrue(isinstance(cmd_float({}, "1"), float))
		self.assertTrue(isinstance(cmd_float({}, "abc"), float))

	def test_string(self):
		self.assertTrue(isinstance(cmd_string({}, 1.0), str))

	def test_bool(self):
		self.assertTrue(isinstance(cmd_bool({}, 1.0), bool))

	def test_undefined(self):
		self.assertEqual(cmd_undefined({}), None)
		