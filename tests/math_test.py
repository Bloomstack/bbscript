import unittest
from bbscript.stdlib.math import cmd_math
from bbscript.stdlib.even_odd import cmd_is_even, cmd_is_odd

class TestMath(unittest.TestCase):

	def test_addition(self):
		self.assertEqual(cmd_math({}, "+", 1, 1), 2)
		self.assertEqual(cmd_math({}, "+", -1, -1), -2)

	def test_substraction(self):
		self.assertEqual(cmd_math({}, "-", 1, 1), 0)
		self.assertEqual(cmd_math({}, "-", -1, -1), 0)

	def test_division(self):
		self.assertEqual(cmd_math({}, "/", 1, 1), 1)
		self.assertEqual(cmd_math({}, "/", -1, -1), 1)

	def test_multiply(self):
		self.assertEqual(cmd_math({}, "*", 1, 1), 1)
		self.assertEqual(cmd_math({}, "*", -1, -1), 1)

	def test_percent(self):
		self.assertEqual(cmd_math({}, "%", 1, 50), .5)
		self.assertEqual(cmd_math({}, "%", 1, 25), .25)

	def test_modulus(self):
		self.assertEqual(cmd_math({}, "MOD", 6, 5), 1)
		self.assertEqual(cmd_math({}, "MOD", 6, -5), 1)
		self.assertEqual(cmd_math({}, "MOD", -6, 5), -1)
		self.assertEqual(cmd_math({}, "MOD", -6, -5), -1)
		self.assertEqual(cmd_math({}, "MOD", 4, 5), 4)
		self.assertEqual(cmd_math({}, "MOD", 4, -5), 4)
		self.assertEqual(cmd_math({}, "MOD", -4, 5), -4)
		self.assertEqual(cmd_math({}, "MOD", -4, -5), -4)
		self.assertRaises(ValueError, lambda: cmd_math({}, "MOD", 0, 0))
		self.assertRaises(ValueError, lambda: cmd_math({}, "MOD", 1, 0))

	def test_wrap(self):
		self.assertEqual(cmd_math({}, "WRAP", 3, 2), 1)
		self.assertEqual(cmd_math({}, "WRAP", -1, 2), 1)
		self.assertRaises(ZeroDivisionError, lambda: cmd_math({}, "WRAP", 0, 0))
		self.assertRaises(ZeroDivisionError, lambda: cmd_math({}, "WRAP", -1, 0))

	def test_is_even(self):
		self.assertTrue(cmd_is_even({}, 0))
		self.assertFalse(cmd_is_even({}, 1))
		self.assertTrue(cmd_is_even({}, 2))

	def test_is_odd(self):
		self.assertFalse(cmd_is_odd({}, 0))
		self.assertTrue(cmd_is_odd({}, 1))
		self.assertFalse(cmd_is_odd({}, 2))

if __name__ == '__main__':
    unittest.main()