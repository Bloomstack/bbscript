import unittest
from bbscript.stdlib import cmd_var, cmd_doc
from bbscript.errors import InvalidOperation

class TestVariables(unittest.TestCase):
	def test_var_get(self):
		doc = {"docname": "testdoc"}
		ctx = {"$test_var": "test value", "$doc": doc}

		self.assertEqual(cmd_var(ctx, "test_var"), "test value")
		self.assertEqual(cmd_var(ctx, "doc"), doc)
		self.assertEqual(cmd_var(ctx, "doc", "docname"), doc.get("docname"))

	def test_doc(self):
		doc = {"field1": "value1", "field2": True, "field3": 123}
		meta = {
			"fields": {
				"field1": {
					"type": "string"
				},
				"field2": {
					"type": "boolean"
				},
				"field3": {
					"type": "int"
				}
			}
		}
		ctx = {
			"$doc": doc
		}
		self.assertEqual(cmd_doc(ctx, "doc", meta), doc)
