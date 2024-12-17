from abc import ABC, abstractmethod
from typing import List

from src.kruskals.disjoint_set import DisjointSet
from src.kruskals.edges import Edge


class MSTStrategy(ABC):
    @abstractmethod
    def find_mst(self, vertices_count: int, edges: List[Edge]) -> List[Edge]:
        pass


class KruskalMST(MSTStrategy):
    def find_mst(self, vertices_count: int, edges: List[Edge]) -> List[Edge]:
        sorted_edges = sorted(edges, key=lambda e: e.weight)
        dsu = DisjointSet(vertices_count)
        mst = []
        for edge in sorted_edges:
            if dsu.union(edge.u, edge.v):
                mst.append(edge)
            if len(mst) == vertices_count - 1:
                break
        if len(mst) != vertices_count - 1:
            return []
        return mst
