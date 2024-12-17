import unittest

from src.kruskals.graph import Graph
from src.kruskals.mst_strategy import KruskalMST


class TestKruskalMST(unittest.TestCase):
    def test_empty_graph(self):
        graph = Graph(1)
        kruskal = KruskalMST()
        mst = kruskal.find_mst(graph.vertices_count, graph.edges)
        self.assertEqual(mst, [])

    def test_single_vertex(self):
        graph = Graph(1)
        kruskal = KruskalMST()
        mst = kruskal.find_mst(graph.vertices_count, graph.edges)
        self.assertEqual(mst, [])

    def test_disconnected_graph(self):
        graph = Graph(4)
        graph.add_edge(0, 1, 1)
        graph.add_edge(2, 3, 2)
        kruskal = KruskalMST()
        mst = kruskal.find_mst(graph.vertices_count, graph.edges)
        self.assertEqual(mst, [])

    def test_normal_graph(self):
        graph = Graph(4)
        graph.add_edge(0, 1, 1)
        graph.add_edge(0, 2, 2)
        graph.add_edge(1, 2, 4)
        graph.add_edge(2, 3, 3)
        kruskal = KruskalMST()
        mst = kruskal.find_mst(graph.vertices_count, graph.edges)
        self.assertEqual(len(mst), 3)
        self.assertEqual(sum(e.weight for e in mst), 6.0)

    def test_equal_weights(self):
        graph = Graph(3)
        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 2, 1)
        graph.add_edge(0, 2, 1)
        kruskal = KruskalMST()
        mst = kruskal.find_mst(graph.vertices_count, graph.edges)
        self.assertEqual(len(mst), 2)
        self.assertEqual(sum(e.weight for e in mst), 2)

    def test_large_line_graph(self):
        n = 50
        graph = Graph(n)
        for i in range(n - 1):
            graph.add_edge(i, i + 1, i + 1)
        kruskal = KruskalMST()
        mst = kruskal.find_mst(graph.vertices_count, graph.edges)
        self.assertEqual(len(mst), n - 1)
        self.assertEqual(sum(e.weight for e in mst), sum(range(1, n)))

    def test_large_complete_graph(self):
        """
        Полный граф из 5 вершин
        Веса постепенно растут
        Вершины: 0,1,2,3,4
        C(5,2) = 10 рёбер
        MST в таком случае - это 4 ребра с наименьшими весами
        """

        graph = Graph(5)
        weight = 1
        for i in range(5):
            for j in range(i + 1, 5):
                graph.add_edge(i, j, weight)
                weight += 1
        kruskal = KruskalMST()
        mst = kruskal.find_mst(graph.vertices_count, graph.edges)
        self.assertEqual(len(mst), 4)
        self.assertEqual(sum(e.weight for e in mst), 10)
