import unittest

from src.kruskals.graph import Graph


class TestGraph(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            Graph(0)
        graph = Graph(3)
        self.assertEqual(graph.vertices_count, 3)

    def test_add_edge_valid(self):
        graph = Graph(3)
        graph.add_edge(0, 1, 1)
        self.assertEqual(len(graph.edges), 1)

    def test_add_edge_invalid_index(self):
        graph = Graph(3)
        with self.assertRaises(ValueError):
            graph.add_edge(-1, 0, 1)
        with self.assertRaises(ValueError):
            graph.add_edge(0, 3, 1)

    def test_add_loop_edge(self):
        graph = Graph(3)
        with self.assertRaises(ValueError):
            graph.add_edge(0, 0, 1)

    def test_add_negative_or_zero_weight(self):
        graph = Graph(3)
        with self.assertRaises(ValueError):
            graph.add_edge(0, 1, -1)
        with self.assertRaises(ValueError):
            graph.add_edge(0, 1, 0)

    def test_max_weight(self):
        graph = Graph(3)
        graph.add_edge(0, 1, 1023)
        self.assertEqual(len(graph.edges), 1)
        self.assertEqual(graph.edges[0].weight, 1023)
        with self.assertRaises(ValueError):
            graph.add_edge(1, 2, 1024)

    def test_large_graph(self):
        n = 50
        graph = Graph(n)
        for i in range(n - 1):
            graph.add_edge(i, i + 1, i + 1)
        self.assertEqual(len(graph.edges), n - 1)
