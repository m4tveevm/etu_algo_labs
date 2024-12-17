import unittest

from src.kruskals.disjoint_set import DisjointSet


class TestDisjointSet(unittest.TestCase):
    def test_init(self):
        dsu = DisjointSet(5)
        for i in range(5):
            self.assertEqual(dsu.find(i), i)

    def test_union_find(self):
        dsu = DisjointSet(5)
        dsu.union(0, 1)
        self.assertEqual(dsu.find(0), dsu.find(1))
        dsu.union(1, 2)
        self.assertEqual(dsu.find(0), dsu.find(2))
        self.assertNotEqual(dsu.find(3), dsu.find(0))

    def test_large(self):
        n = 50
        dsu = DisjointSet(n)
        for i in range(n - 1):
            dsu.union(i, i + 1)
        root = dsu.find(0)
        for i in range(1, n):
            self.assertEqual(dsu.find(i), root)

    def test_no_unions(self):
        n = 10
        dsu = DisjointSet(n)
        for i in range(n):
            self.assertEqual(dsu.find(i), i)
