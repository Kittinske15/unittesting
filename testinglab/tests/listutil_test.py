import unittest
from listutil import count_unique
from listutil import binary_search

class TestCountUnique(unittest.TestCase):
    def borderline_cases(self):
        list = []
        self.assertEqual(0,count_unique(list))

    def typical_cases(self):
        list = ["a","a","b","c"]
        self.assertEqual(3,count_unique(list))

    def unique_cases(self):
        list = [1,2,3,4,5,6]
        self.assertEqual(6,count_unique(list))

    def extreme_cases(self):
        list = [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]
        self.assertEqual(1,count_unique(list))

class TestBinarySearch(unittest.TestCase):
    def typical_search(self):
        list = [2,4,6,1,3]
        self.assertEqual(binary_search(list, 3), 2)

    def none_search(self):
        binary_search([1,3,5,2,7,90],None)
        self.assertRaises(TypeError,"Input couldn't be None")

    def unexpected_search(self):
        self.assertIsNone(binary_search([1,2], 6),"None")

    def extreme_search(self):
        self.assertEqual(binary_search(binary_search([range(10000)],5),6))

