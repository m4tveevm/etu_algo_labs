import random
import unittest

from solution import timsort


class TestTimSort(unittest.TestCase):
    def test_empty_array(self):
        arr = []
        timsort(arr)
        self.assertEqual(arr, [])

    def test_single_element(self):
        arr = [1]
        timsort(arr)
        self.assertEqual(arr, [1])

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        timsort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_array(self):
        arr = [5, 4, 3, 2, 1]
        timsort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_random_array(self):
        arr = [3, 1, 4, 5, 2]
        timsort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_duplicates(self):
        arr = [1, 3, 2, 1, 3, 2]
        timsort(arr)
        self.assertEqual(arr, [1, 1, 2, 2, 3, 3])


    def test_large_array(self):
        arr = list(range(10000, 0, -1))
        expected = sorted(arr)
        timsort(arr)
        self.assertEqual(arr, expected)



