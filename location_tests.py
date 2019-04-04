import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        "runs multiple test cases checking the repr function"
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc1),"Location('SLO', 35.3, -120.7)")
        loc2 = Location("Cal Poly", 32.5, -500)
        self.assertEqual(repr(loc2),"Location('Cal Poly', 32.5, -500)")
        loc3 = Location("Cal Poly", 32.5, -500)
        self.assertNotEqual(repr(loc3),"Location('SLO', 35.3, -120.7)")
        loc4 = Location("Poly Canyon Village", -500000, 0.5)
        self.assertNotEqual(repr(loc4),"Location('SLO', 35.3, -120.7)")
        loc5 = Location("Poly Canyon Village", -500000, 0.5)
        self.assertEqual(repr(loc5),"Location('Poly Canyon Village', -500000, 0.5)")

    def test_eq(self):
        "runs multiple test cases checking the equal sign"
        loc6 = Location("SLO", 35.3, -120.7)
        loc7 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc6 == loc7, True)
        loc8 = Location("SLO", 35.3, -120.7)
        loc9 = Location("Cal Poly", 32.5, -500)
        self.assertEqual(loc8 == loc9, False)
        loc10 = Location("Cal Poly", 32.5, -500)
        loc11 = Location("Cal Poly", 32.5, -500)
        self.assertEqual(loc10 == loc11, True)
        loc12 = Location("Poly Canyon Village", -500000, 0.5)
        loc13 = Location("Poly Canyon Village", -500000, 0.5)
        self.assertEqual(loc12 == loc13, True)
        loc14 = Location("SLO", 35.3, -120.7)
        loc15 = Location("Poly Canyon Village", -500000, 0.5)
        self.assertEqual(loc14 == loc15, False)


if __name__ == "__main__":
        unittest.main()
