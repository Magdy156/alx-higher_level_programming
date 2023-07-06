#!/usr/bin/python3
import unittest
import sys
sys.path.append('/home/magdy/Desktop/alx-higher_level_programming/0x07-python-test_driven_development')
add_integer = __import__('0-add_integer').add_integer

class TestFile1(unittest.TestCase):
    
	def test_functionality1(self):
		self.assertEqual(add_integer(2, 3), 5)
	def test_functionality2(self):
		self.assertEqual(add_integer(2, -3), -1)
	def test_functionality3(self):
		self.assertEqual(add_integer(5.0, 6.0), 11)
	def test_functionality4(self):
		self.assertEqual(add_integer(1.6, 0.4), 1)
	def test_functionality5(self):
		self.assertEqual(add_integer(-1.6, -0.4), -1)
	def test_functionality6(self):
		self.assertEqual(add_integer(2),100)
	def test_functionality7(self):
		with self.assertRaises(TypeError):
			add_integer("hey", 0.4)
	def test_functionality8(self):
		with self.assertRaises(TypeError):
			add_integer(1.6, "hey")
	def test_functionality9(self):
		with self.assertRaises(TypeError):
			add_integer(None)
	

if __name__ == '__main__':
    unittest.main()
