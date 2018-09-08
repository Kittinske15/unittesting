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
        list = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(list, 4), 3)
        list = [1, 4, 7, 8, 9, 10, 11, 12, 17, 25]
        self.assertEqual(binary_search(list, 9), 4)

