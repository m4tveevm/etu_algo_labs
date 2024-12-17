from copy import copy
from typing import List

from src.kruskals.edges import Edge


class Graph:
    def __init__(self, vertices_count: int):
        if vertices_count <= 0:
            raise ValueError("Количество вершин <= 0")
        self.vertices_count = vertices_count
        self._edges: List[Edge] = []

    @property
    def edges(self) -> List[Edge]:
        return copy(self._edges)

    def add_edge(self, begin: int, end: int, weight: float):
        if (
            begin < 0
            or end < 0
            or begin >= self.vertices_count
            or end >= self.vertices_count
        ):
            raise ValueError("Неверный индекс вершины")
        if begin == end:
            raise ValueError("Петли не допускаются")
        if weight <= 0 or weight > 1023:
            raise ValueError(
                "Вес ребра должен быть в диапазоне [1, ..., 1023]"
            )
        self._edges.append(Edge(begin, end, weight))
