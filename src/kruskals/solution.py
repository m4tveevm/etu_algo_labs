from src.kruskals.graph_reader import GraphReader
from src.kruskals.mst_strategy import KruskalMST


def main():
    input_file = "input.txt"
    output_file = "output.txt"

    reader = GraphReader()
    graph, vertex_names = reader.read_graph_from_file(input_file)

    kruskal = KruskalMST()
    mst = kruskal.find_mst(graph.vertices_count, graph.edges)

    if not mst:
        with open(output_file, "w", encoding="utf-8") as out:
            out.write("Остов не существует\n")
        return

    named_edges = []
    for edge in mst:
        v1_name = vertex_names[edge.u]
        v2_name = vertex_names[edge.v]
        if v1_name > v2_name:
            v1_name, v2_name = v2_name, v1_name
        named_edges.append((v1_name, v2_name, edge.weight))

    named_edges.sort(key=lambda x: (x[0], x[1]))
    total_weight = sum(edge[2] for edge in named_edges)

    with open(output_file, "w", encoding="utf-8") as out:
        for u_name, v_name, w in named_edges:
            out.write(f"{u_name} {v_name}\n")
        out.write(f"{total_weight}\n")


if __name__ == "__main__":
    main()
