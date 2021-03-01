import unittest
from bbscript.commands import cmd_math

class TestMath(unittest.TestCase):

	def test_addition(self):
		self.assertEqual(cmd_math({}, "+", 1, 1), 2)
		self.assertEqual(cmd_math({}, "+", -1, -1), -2)

	def test_substraction(self):
		self.assertEqual(cmd_math({}, "-", 1, 1), 0)
		self.assertEqual(cmd_math({}, "-", -1, -1), 0)
		
if __name__ == '__main__':
    unittest.main()