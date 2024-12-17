from dataclasses import dataclass


@dataclass(frozen=True)
class Edge:
    u: int
    v: int
    weight: float
