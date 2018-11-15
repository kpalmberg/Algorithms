import unittest
from euclids_algorithm import *

class TestGCDFunctions(unittest.TestCase):

    def test_GCD_Method1(self):
        self.assertEqual(GCD_Method1(10, 15), 5)
        self.assertEqual(GCD_Method1(50, 15), 5)
        self.assertEqual(GCD_Method1(100, 15), 5)
        self.assertEqual(GCD_Method1(24, 54), 6)
        self.assertEqual(GCD_Method1(100, 30), 10)
        self.assertEqual(GCD_Method1(270, 192), 6)
        self.assertEqual(GCD_Method1(24, 36), 12)

    def test_GCD_Method2(self):
        pass
        self.assertEqual(GCD_Method2(10, 15), 5)
        self.assertEqual(GCD_Method2(50, 15), 5)
        self.assertEqual(GCD_Method2(100, 15), 5)
        self.assertEqual(GCD_Method2(24, 54), 6)
        self.assertEqual(GCD_Method2(100, 30), 10)
        self.assertEqual(GCD_Method2(270, 192), 6)
        self.assertEqual(GCD_Method2(24, 36), 12)
