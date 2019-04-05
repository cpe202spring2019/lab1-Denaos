import unittest
from lab1 import *


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

    def test_reverse_rec_error(self):
        """"Tests the reverse_rec function if the list is none"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

    def test_reverse_rec_empty(self):
        """"Tests the reverse_rec function if the list is empty"""
        tlist = []
        self.assertEqual(reverse_rec(tlist), [])

    def test_reverse_rec_float(self):
        """Tests the reverse_rec function with floating values"""
        self.assertEqual(reverse_rec([1.01,5.05,9.09]),[9.09,5.05,1.01])

    def test_reverse_rec_str(self):
        """Tests the reverse_rec function with a string in the list"""
        self.assertEqual(reverse_rec(["string",5,1]),[1,5,"string"])
        self.assertEqual(reverse_rec([1,"string",5]),[5,"string",1])
        self.assertEqual(reverse_rec([5,1,"string"]),["string",1,5])

    def test_reverse_rec_order(self):
        """Tests the reverse_rec function with an order"""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([3,1,2]),[2,1,3])
        self.assertEqual(reverse_rec([2,3,1]),[1,3,2])

    def test_bin_search_error(self):
        """"Tests the bin_search function for a value error"""
        list_val =None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(list_val)

    def test_bin_search_empty(self):
        list_val=[]
        self.assertEqual(bin_search(20,0,len(list_val)-1,list_val),None)

    def test_bin_search_str(self):
        list_val =["string",10,100,1000,2000,5000,10000,20000,50000]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search("string",low,high,list_val),"string")

    def test_bin_search_order(self):
        """Tests the bin_search function with an order"""
if __name__ == "__main__":
    unittest.main()


