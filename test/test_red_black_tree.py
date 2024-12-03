import unittest

from src.tree.red_black_tree import RedBlackTree
from src.tree.traversal import (
    BreadthFirstTraversal,
    InOrderTraversal,
    PostOrderTraversal,
    PreOrderTraversal,
)


class TestRedBlackTree(unittest.TestCase):
    def setUp(self):
        self.tree = RedBlackTree()
        self.values = [20, 15, 25, 10, 18, 22, 30, 5, 12, 17, 19]
        for val in self.values:
            self.tree.insert(val)

    @staticmethod
    def is_valid_red_black_tree(tree):
        """
        Checks whether the given red-black tree satisfies all red-black tree properties:

        1. Every node is either red or black.
        2. The root of the tree is black.
        3. All leaves (NIL nodes) are black.
        4. If a node is red, both its children must be black
           (i.e., no two consecutive red nodes are allowed).
        5. For each node, all paths from that node to its descendant leaves
           must contain the same number of black nodes (black height).

        Returns:
            bool: True if the tree satisfies all properties, False otherwise.
        """

        def check_properties(node):
            if node == tree.nil:
                return 1

            if node.color not in ("RED", "BLACK"):
                return -1

            if node.color == "RED":
                if (
                    node.get_left().color != "BLACK"
                    or node.get_right().color != "BLACK"
                ):
                    return -1

            left_black_height = check_properties(node.get_left())
            right_black_height = check_properties(node.get_right())
            if left_black_height == -1 or right_black_height == -1:
                return -1

            if left_black_height != right_black_height:
                return -1

            return left_black_height + (1 if node.color == "BLACK" else 0)

        if tree.root.color != "BLACK":
            return False

        result = check_properties(tree.root)
        return result != -1

    def test_insert(self):
        traversal = InOrderTraversal()
        result = self.tree.traverse(traversal)
        expected = sorted(self.values)
        self.assertEqual(result, expected)
        self.assertTrue(self.is_valid_red_black_tree(self.tree))

    def test_insert_duplicate(self):
        initial_size = len(self.tree.traverse(InOrderTraversal()))
        self.tree.insert(20)
        new_size = len(self.tree.traverse(InOrderTraversal()))
        self.assertEqual(initial_size + 1, new_size)
        self.assertTrue(self.is_valid_red_black_tree(self.tree))

    def test_search(self):
        for val in self.values:
            node = self.tree.search(val)
            self.assertIsNotNone(node)
            self.assertEqual(node.get_value(), val)
        self.assertEqual(self.tree.search(100), self.tree.nil)

    def test_delete(self):
        self.tree.delete(15)
        self.tree.delete(22)
        traversal = InOrderTraversal()
        result = self.tree.traverse(traversal)
        expected = sorted([val for val in self.values if val not in [15, 22]])
        self.assertEqual(result, expected)
        self.assertTrue(self.is_valid_red_black_tree(self.tree))

    def test_delete_nonexistent(self):
        result = self.tree.delete(100)
        self.assertFalse(result)

    def test_traversals(self):
        strategies = {
            "preorder": PreOrderTraversal(),
            "inorder": InOrderTraversal(),
            "postorder": PostOrderTraversal(),
            "breadth_first": BreadthFirstTraversal(),
        }
        for name, strategy in strategies.items():
            result = self.tree.traverse(strategy)
            self.assertIsInstance(result, list)
            self.assertEqual(len(result), len(self.values))

    def test_balance(self):
        self.assertTrue(self.is_valid_red_black_tree(self.tree))

    def test_insert_case1(self):
        tree = RedBlackTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        tree.insert(1)
        tree.insert(7)
        tree.insert(13)
        tree.insert(17)
        tree.insert(6)
        self.assertTrue(self.is_valid_red_black_tree(tree))

    def test_insert_case2_case3(self):
        tree = RedBlackTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        tree.insert(1)
        tree.insert(7)
        tree.insert(6)
        self.assertTrue(self.is_valid_red_black_tree(tree))

        tree = RedBlackTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        tree.insert(12)
        tree.insert(17)
        tree.insert(19)
        self.assertTrue(self.is_valid_red_black_tree(tree))

    def test_delete_cases(self):
        tree = RedBlackTree()
        values = [20, 15, 25, 10, 18, 22, 30, 5, 12, 17, 19]
        for val in values:
            tree.insert(val)

        tree.delete(5)
        self.assertTrue(self.is_valid_red_black_tree(tree))

        tree.delete(22)
        self.assertTrue(self.is_valid_red_black_tree(tree))

        tree.delete(15)
        self.assertTrue(self.is_valid_red_black_tree(tree))

        tree.delete(20)
        self.assertTrue(self.is_valid_red_black_tree(tree))

    def test_delete_case2(self):
        tree = RedBlackTree()
        tree.insert(1)
        tree.insert(2)
        tree.insert(3)
        tree.delete(1)
        self.assertTrue(self.is_valid_red_black_tree(tree))

    def test_delete_case3(self):
        tree = RedBlackTree()
        tree.insert(3)
        tree.insert(2)
        tree.insert(4)
        tree.insert(1)
        tree.delete(4)
        self.assertTrue(self.is_valid_red_black_tree(tree))

    def test_delete_case4(self):
        tree = RedBlackTree()
        tree.insert(3)
        tree.insert(1)
        tree.insert(5)
        tree.insert(0)
        tree.insert(2)
        tree.insert(4)
        tree.insert(6)
        tree.delete(0)
        tree.delete(2)
        self.assertTrue(self.is_valid_red_black_tree(tree))

    def test_delete_case5(self):
        tree = RedBlackTree()
        tree.insert(11)
        tree.insert(2)
        tree.insert(14)
        tree.insert(1)
        tree.insert(7)
        tree.insert(15)
        tree.insert(5)
        tree.insert(8)
        tree.insert(4)
        tree.delete(1)
        tree.delete(2)
        self.assertTrue(self.is_valid_red_black_tree(tree))
