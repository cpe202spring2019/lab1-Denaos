import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc1),"Location('SLO', 35.3, -120.7)")

    # Add more tests!
    def test_repr2(self):
        loc2 = Location("Cal Poly", 32.5, -500)
        self.assertEqual(repr(loc2),"Location('Cal Poly', 32.5, -500)")

    def test_repr3(self):
        loc3 = Location("Cal Poly", 32.5, -500)
        self.assertNotEqual(repr(loc3),"Location('SLO', 35.3, -120.7)")

    def test_repr4(self):
        loc4 = loc1
        self.assertEqual(repr(loc4),"Location('SLO', 35.3, -120.7)")

    def test_repr5(self):
        loc5 = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc5),"Location('SLO', 35.3, -120.7)")

    def test_eq(self):
        loc6 = loc1
        self.assertEqual(eq(loc6, loc1), print(True))
if __name__ == "__main__":
        unittest.main()
