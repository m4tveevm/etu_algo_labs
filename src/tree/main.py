from src.tree.binary_tree import BinaryTree
from src.tree.parser import TreeParser
from src.tree.red_black_tree import RedBlackTree
from src.tree.traversal import (
    BreadthFirstTraversal,
    InOrderTraversal,
    PostOrderTraversal,
    PreOrderTraversal,
)


def read_tree_from_file(filename):
    with open(filename, "r") as file:
        tree_string = file.read().strip()
        parser = TreeParser(tree_string)
        root = parser.parse()
        return root


def build_red_black_tree(binary_root):
    rb_tree = RedBlackTree()

    def insert_node(node):
        if node:
            try:
                value = int(node.get_value())
            except ValueError:
                value = node.get_value()
            rb_tree.insert(value)
            insert_node(node.get_left())
            insert_node(node.get_right())

    insert_node(binary_root)
    return rb_tree


def demonstrate_traversals(tree):
    strategies = {
        "Обход в ширину": BreadthFirstTraversal(),
        "Обход в глубину (прямой)": PreOrderTraversal(),
        "Обход в глубину (симметричный)": InOrderTraversal(),
        "Обход в глубину (обратный)": PostOrderTraversal(),
    }

    for name, strategy in strategies.items():
        result = tree.traverse(strategy)
        print(f"{name}: {' '.join(map(str, result))}")


if __name__ == "__main__":
    filename = "tree.txt"
    binary_root = read_tree_from_file(filename)
    if not binary_root:
        print("Не удалось построить дерево.")
        exit(1)
    binary_tree = BinaryTree(binary_root)
    print("Построено двоичное дерево.")
    demonstrate_traversals(binary_tree)

    print("\nПостроение красно-черного дерева из двоичного дерева...")
    rb_tree = build_red_black_tree(binary_root)
    print("Вывод узлов красно-черного дерева:")
    demonstrate_traversals(rb_tree)
