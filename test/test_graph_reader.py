import os
import unittest

from src.kruskals.graph_reader import GraphReader


class TestGraphReader(unittest.TestCase):
    def setUp(self):
        self.test_filename = "input.txt"

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_empty_file(self):
        open(self.test_filename, "w").close()
        reader = GraphReader()
        with self.assertRaises(ValueError):
            reader.read_graph_from_file(self.test_filename)

    def test_wrong_format(self):
        with open(self.test_filename, "w") as file:
            file.write("A B C\n0 1 2\n0 0")
        reader = GraphReader()
        with self.assertRaises(ValueError):
            reader.read_graph_from_file(self.test_filename)

    def test_too_many_vertices(self):
        names = " ".join([f"V{i}" for i in range(51)])
        with open(self.test_filename, "w") as file:
            file.write(names + "\n")
        reader = GraphReader()
        with self.assertRaises(ValueError):
            reader.read_graph_from_file(self.test_filename)

    def test_invalid_weight(self):
        with open(self.test_filename, "w") as file:
            file.write("A B\n0 1024\n1024 0\n")
        reader = GraphReader()
        with self.assertRaises(ValueError):
            reader.read_graph_from_file(self.test_filename)

    def test_valid_graph(self):
        with open(self.test_filename, "w") as file:
            file.write("A B C\n0 3 1\n3 0 2\n1 2 0\n")
        reader = GraphReader()
        graph, names = reader.read_graph_from_file(self.test_filename)
        self.assertEqual(len(names), 3)
        self.assertEqual(graph.vertices_count, 3)
        self.assertEqual(len(graph.edges), 3)
        weights = sorted(edge.weight for edge in graph.edges)
        self.assertEqual(weights, [1, 2, 3])

    def test_full_graph(self):
        """
        Полный граф из 4 вершин
        Вершины: A B C D
        Матрица:
        0 1 2 3
        1 0 4 5
        2 4 0 6
        """

        with open(self.test_filename, "w") as file:
            file.write("A B C D\n")
            file.write("0 1 2 3\n")
            file.write("1 0 4 5\n")
            file.write("2 4 0 6\n")
            file.write("3 5 6 0\n")
        reader = GraphReader()
        g, names = reader.read_graph_from_file(self.test_filename)
        self.assertEqual(len(g.edges), 6)
        self.assertEqual(sorted(names), ["A", "B", "C", "D"])
