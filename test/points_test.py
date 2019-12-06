# -*- coding: utf-8 -*-
from points import *
import unittest

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.zero = Point(0, 0)

    def test_str(self):
        self.assertEqual(str(Point(5, 4)), "(5,4)")
        self.assertEqual(str(Point(-15, -4)), "(-15,-4)")
        self.assertEqual(str(Point(10, 4)), "(10,4)")
        self.assertEqual(str(Point(5, -4)), "(5,-4)")

    def test_repr(self):
        self.assertEqual(repr(Point(5, 4)), "Point(5,4)")
        self.assertEqual(repr(Point(-15, -4)), "Point(-15,-4)")
        self.assertEqual(repr(Point(10, 4)), "Point(10,4)")
        self.assertEqual(repr(Point(5, -4)), "Point(5,-4)")

    def test_add(self):
        self.assertEqual(self.zero + self.zero, self.zero)
        self.assertEqual(Point(0, 1) + Point(0, 1), Point(0, 2))
        self.assertEqual(Point(10, 1) + Point(0, 1), Point(10, 2))
        self.assertEqual(Point(-5, -5) + Point(2, 1), Point(-3, -4))
        self.assertEqual(Point(100, 100) + Point(100, 100), Point(200, 200))

    def test_sub(self):
        self.assertEqual(self.zero - self.zero, self.zero)
        self.assertEqual(Point(0, 1) - Point(0, 1), Point(0, 0))
        self.assertEqual(Point(10, 1) - Point(0, 1), Point(10, 0))
        self.assertEqual(Point(-3, 1) - Point(10, -6), Point(-13, 7))
        self.assertEqual(Point(25, 15) - Point(23, 13), Point(2, 2))

    def test_length(self):
        self.assertEqual(Point(5, 1).length(), math.sqrt(26))
        self.assertEqual(Point(-4, 3).length(), 5)
        self.assertEqual(Point(1, 0).length(), 1)
        self.assertEqual(Point(5, 5).length(), math.sqrt(50))
        
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

