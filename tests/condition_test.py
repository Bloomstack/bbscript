import unittest
from bbscript.stdlib import cmd_condition, cmd_if
from bbscript.errors import InvalidOperation

class TestCondition(unittest.TestCase):

	def test_equals(self):
		self.assertTrue(cmd_condition({}, "==", 1, 1))
		self.assertTrue(cmd_condition({}, "==", 1, 1.0))
		self.assertTrue(cmd_condition({}, "==", "a", "a"))
		self.assertTrue(cmd_condition({}, "==", True, True))
		self.assertTrue(cmd_condition({}, "==", False, False))
		self.assertFalse(cmd_condition({}, "==", 1, 0))
		self.assertFalse(cmd_condition({}, "==", "a", "b"))
		self.assertFalse(cmd_condition({}, "==", True, False))
		self.assertFalse(cmd_condition({}, "==", False, True))

	def test_not_equals(self):
		self.assertFalse(cmd_condition({}, "!=", 1, 1))
		self.assertFalse(cmd_condition({}, "!=", 1, 1.0))
		self.assertFalse(cmd_condition({}, "!=", "a", "a"))
		self.assertFalse(cmd_condition({}, "!=", True, True))
		self.assertFalse(cmd_condition({}, "!=", False, False))
		self.assertTrue(cmd_condition({}, "!=", 1, 0))
		self.assertTrue(cmd_condition({}, "!=", "a", "b"))
		self.assertTrue(cmd_condition({}, "!=", True, False))
		self.assertTrue(cmd_condition({}, "!=", False, True))

	def test_like(self):
		self.assertTrue(cmd_condition({}, "~", "this is some text", "is"))
		self.assertTrue(cmd_condition({}, "~", "this is some text", "is text"))
		self.assertTrue(cmd_condition({}, "~", "this is some text", "this%is.text"))
		self.assertTrue(cmd_condition({}, "~", "this IS some text", "iS"))
		self.assertTrue(cmd_condition({}, "~", "this is SOME text", "Is tExt"))
		self.assertTrue(cmd_condition({}, "~", "this is some TEXT", "thiS%is.tEXt"))

	def test_not_like(self):
		self.assertTrue(cmd_condition({}, "!~", "this is some text", "nothing like it"))
		self.assertTrue(cmd_condition({}, "!~", "this is some text", "nothing like"))
		self.assertTrue(cmd_condition({}, "!~", "this is some text", "nothing it"))

	def test_greater_than(self):
		self.assertTrue(cmd_condition({}, ">", 2, 1))
		self.assertFalse(cmd_condition({}, ">", 1, 1))
		self.assertTrue(cmd_condition({}, ">", "b", "a"))
		self.assertFalse(cmd_condition({}, ">", "a", "b"))
		self.assertTrue(cmd_condition({}, ">", "ba", "a"))
		self.assertTrue(cmd_condition({}, ">", "ba", "b"))

	def test_greater_and_equal_than(self):
		self.assertTrue(cmd_condition({}, ">=", 2, 1))
		self.assertTrue(cmd_condition({}, ">=", 1, 1))
		self.assertTrue(cmd_condition({}, ">=", "b", "a"))
		self.assertFalse(cmd_condition({}, ">=", "a", "b"))
		self.assertTrue(cmd_condition({}, ">=", "ba", "a"))
		self.assertTrue(cmd_condition({}, ">=", "ba", "b"))

	def test_less_than(self):
		self.assertTrue(cmd_condition({}, "<", 1, 2))
		self.assertFalse(cmd_condition({}, "<", 1, 1))
		self.assertFalse(cmd_condition({}, "<", "b", "a"))
		self.assertTrue(cmd_condition({}, "<", "a", "b"))
		self.assertFalse(cmd_condition({}, "<", "ba", "a"))
		self.assertFalse(cmd_condition({}, "<", "ba", "b"))

	def test_less_and_equal_than(self):
		self.assertTrue(cmd_condition({}, "<=", 1, 2))
		self.assertTrue(cmd_condition({}, "<=", 1, 1))
		self.assertFalse(cmd_condition({}, "<=", "b", "a"))
		self.assertTrue(cmd_condition({}, "<=", "a", "b"))
		self.assertFalse(cmd_condition({}, "<=", "ba", "a"))
		self.assertFalse(cmd_condition({}, "<=", "ba", "b"))

	def test_and(self):
		self.assertTrue(cmd_condition({}, "AND", True, True))
		self.assertFalse(cmd_condition({}, "AND", True, False))
		self.assertFalse(cmd_condition({}, "AND", False, False))
		self.assertFalse(cmd_condition({}, "AND", False, True))

	def test_or(self):
		self.assertTrue(cmd_condition({}, "OR", True, True))
		self.assertTrue(cmd_condition({}, "OR", True, False))
		self.assertFalse(cmd_condition({}, "OR", False, False))
		self.assertTrue(cmd_condition({}, "OR", False, True))

	def test_not(self):
		self.assertFalse(cmd_condition({}, "NOT", True, True))
		self.assertTrue(cmd_condition({}, "NOT", True, False))
		self.assertTrue(cmd_condition({}, "NOT", False, False))
		self.assertTrue(cmd_condition({}, "NOT", False, True))

	def test_xor(self):
		self.assertFalse(cmd_condition({}, "XOR", True, True))
		self.assertTrue(cmd_condition({}, "XOR", True, False))
		self.assertFalse(cmd_condition({}, "XOR", False, False))
		self.assertTrue(cmd_condition({}, "XOR", False, True))

	def test_in(self):
		self.assertTrue(cmd_condition({}, "IN", "abcdefg", "cde"))
		self.assertFalse(cmd_condition({}, "IN", "abcdefg", "123"))

	def test_not_in(self):
		self.assertFalse(cmd_condition({}, "NOT IN", "abcdefg", "cde"))
		self.assertTrue(cmd_condition({}, "NOT IN", "abcdefg", "123"))

	def test_invalid_op(self):
		self.assertRaises(InvalidOperation, lambda: cmd_condition({}, "WTF", True, True))

	def test_if(self):
		self.assertEqual(cmd_if({}, True, ["true"], ["false"]), ["true"])
		self.assertEqual(cmd_if({}, False, ["true"], ["false"]), ["false"])

if __name__ == '__main__':
    unittest.main()