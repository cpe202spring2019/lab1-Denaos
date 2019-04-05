import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        "runs multiple test cases checking the repr function"
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        loc = Location("Cal Poly", 32.5, -500)
        self.assertEqual(repr(loc),"Location('Cal Poly', 32.5, -500)")
        loc = Location("Cal Poly", 32.5, -500)
        self.assertNotEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        loc = Location("Poly Canyon Village", -500000, 0.5)
        self.assertNotEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        loc = Location("Poly Canyon Village", -500000, 0.5)
        self.assertEqual(repr(loc),"Location('Poly Canyon Village', -500000, 0.5)")

    def test_eq_true_false(self):
        "runs multiple test cases checking the equal sign"
        loc = Location("SLO", 35, -120)
        loc2 = Location("SLO", 35, -120)
        self.assertEqual(loc == loc2, True)
        loc = Location("SLO", 35, -120)
        loc2 = Location("Cal Poly", 32, -500)
        self.assertEqual(loc == loc2, False)

    def test_eq_location(self):
        "tests the eq function for the same type"
        loc10 = Location("Cal Poly", 32.5, -500)
        loc11 = 400
        self.assertEqual(loc10 == loc11, False)

    def test_eq_float(self):
        loc12 = Location("Poly Canyon Village", -500.007, 0.5)
        loc13 = Location("Poly Canyon Village", -500.007, 0.5)
        self.assertAlmostEqual(loc12 == loc13, True)
        loc14 = Location("SLO", 35.3, -120.7)
        loc15 = Location("Poly Canyon Village", -500.007, 0.5)
        self.assertAlmostEqual(loc14 == loc15, False)

if __name__ == "__main__":
        unittest.main()
