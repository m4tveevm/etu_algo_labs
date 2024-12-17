from src.kruskals.graph import Graph


def _process_edge(i: int, j: int, val: int, graph: Graph):
    if val == 0:
        return
    if val < 1 or val > 1023:
        raise ValueError("Вес ребра должен быть в диапазоне [1..1023].")
    if j > i:
        graph.add_edge(i, j, val)


def _read_matrix_row(file_obj, vertices_count: int):
    line = file_obj.readline().strip()
    if not line:
        raise ValueError("Строк в матрице меньше, чем количество вершин.")

    row_values = line.split()
    if len(row_values) != vertices_count:
        raise ValueError(
            "Количество столбцов матрицы не соответствует количеству вершин."
        )
    return row_values


def _read_adjacency_matrix(file_obj, graph: Graph):
    vertices_count = graph.vertices_count
    for i in range(vertices_count):
        row_values = _read_matrix_row(file_obj, vertices_count)
        for j, val_str in enumerate(row_values):
            val = int(val_str)
            _process_edge(i, j, val, graph)


class GraphReader:
    def __init__(self, max_vertices=50):
        self.max_vertices = max_vertices

    def read_graph_from_file(self, filename: str):
        with open(filename, "r", encoding="utf-8") as f:
            vertex_names = self._read_vertex_names(f)
            graph = Graph(len(vertex_names))
            _read_adjacency_matrix(f, graph)
            return graph, vertex_names

    def _read_vertex_names(self, file_obj):
        first_line = file_obj.readline().strip()
        if not first_line:
            raise ValueError("File is corrupt")

        vertex_names = first_line.split()
        if len(vertex_names) > self.max_vertices:
            raise ValueError(
                f"Слишком много вершин. Максимум {self.max_vertices}."
            )
        return vertex_names
