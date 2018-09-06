import unittest
from testinglab import listutil
from testinglab.listutil import count_unique

class Test(unittest.TestCase):
    def boarderline_cases(self):
        list = []
        self.assertEqual(0,count_unique(list))

    def typical_cases(self):
        list = ["a","a","b","c"]
        self.assertEqual(3,count_unique(list))

    def impossible_cases(self):
        list = 10
        self.assertFalse(IndexError,count_unique(list))

    def extreme_cases(self):
        list = [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]
        self.assertEqual(1,count_unique(list))