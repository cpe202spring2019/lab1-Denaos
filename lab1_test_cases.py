import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter_error(self):
        """Tests the max_list_iter function for the value error"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_empty(self):
        """"Tests the max_list_iter function if the list is empty"""
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)

    def test_max_list_iter_order(self):
        """"Tests the max_list_iter function of the order of the numbers"""
        tlist = [500, 10, 11, 25]
        self.assertEqual(max_list_iter(tlist), 500)
        tlist = [10, 500, 11, 25]
        self.assertEqual(max_list_iter(tlist), 500)
        tlist = [10, 11, 500, 25]
        self.assertEqual(max_list_iter(tlist), 500)
        tlist = [10, 11, 25, 500]
        self.assertEqual(max_list_iter(tlist), 500)

    def test_max_list_iter_neg(self):
        """""Tests the max_list_iter function with negative values"""
        tlist = [-100, -50, -25, -10]
        self.assertEqual(max_list_iter(tlist), -10)
        tlist = [-5000, -7500, -2500, -1000]
        self.assertEqual(max_list_iter(tlist), -1000)
        tlist = [-50, -49, -51, -10, -75, -99]
        self.assertEqual(max_list_iter(tlist), -10)

    def test_max_list_iter_float(self):
        """"Tests the max_list_iter function with floating values"""
        tlist = [1.01, 1.25, 1.005, 1.34, 1.02]
        self.assertEqual(max_list_iter(tlist), 1.34)
        tlist = [25.25, 10.10, 35.35, 9.09]
        self.assertEqual(max_list_iter(tlist), 35.35)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

if __name__ == "__main__":
        unittest.main()

    
