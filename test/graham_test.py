# -*- coding: utf-8 -*-
from graham import *
import unittest

class TestGraham(unittest.TestCase):
    def setUp(self):
        pass

    def test_graham(self):
        self.assertEqual(graham([Point(0, 0), Point(1, 1), Point(2, 2)]), [Point(0, 0), Point(2, 2)])

        self.assertEqual(graham([Point(0, 0), Point(1,1)]), [Point(0, 0), Point(1, 1)])

        self.assertEqual(graham([Point(0, 0)]), [Point(0, 0)])

        self.assertEqual(graham([Point(0, 0), Point(1, 1),Point(2, 2), Point(3, 5)]), [Point(0, 0), Point(2, 2), Point(3, 5)])
        
        self.assertEqual(graham([Point(0, 3), Point(1, 1), Point(2, 2), Point(4, 4), Point(0, 0), Point(1, 2), Point(3, 1), Point(3, 3)]),
                         [Point(0, 0), Point(3, 1), Point(4, 4), Point(0, 3)])
        
        self.assertEqual(graham([Point(0, 3), Point(1, 1), Point(2, 2), Point(2, 1), Point(0, 0), Point(3, 0), Point(3, 3)]),
                         [Point(0, 0), Point(3, 0), Point(3, 3), Point(0, 3)])

        self.assertEqual(graham([Point(2, 6), Point(3, 5), Point(0.1, 4), Point(2.1, 4), Point(6, 6), Point(6.1, 4), Point(1.3, 3), Point(3, 3),
                                 Point(5.3, 3), Point(0, 2), Point(2.1, 2), Point(4.1, 2), Point(6.1, 2), Point(3, 1), Point(2, 0), Point(4, 0)]),
                         [Point(2, 0), Point(4, 0), Point(6.1, 2), Point(6.1, 4), Point(6, 6), Point(2, 6), Point(0.1, 4), Point(0, 2)])

        self.assertEqual(graham([Point(1, 1), Point(2, 1), Point(3, 1), Point(4, 1), Point(5, 1), Point(6, 3), Point(3, 2), Point (6, 5),
                                 Point(3, 5), Point(1,5), Point(4, 2), Point(2, 3), Point(5, 2.5)]),
                                [Point(1, 1), Point(5, 1), Point(6, 3), Point(6, 5), Point(1, 5)])

        self.assertEqual(graham([Point(0, 0), Point(0, 1), Point(0, 2), Point(1, 0), Point(1, 1), Point(1, 2), Point(2, 0), Point(2, 1), Point(2, 2)]),
                         [Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

