import unittest

from src.tree.binary_tree import BinaryTree
from src.tree.nodes import BinaryTreeNode
from src.tree.traversal import (
    BreadthFirstTraversal,
    InOrderTraversal,
    PostOrderTraversal,
    PreOrderTraversal,
)


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        #       8
        #      / \
        #     5   9
        self.root = BinaryTreeNode(8)
        self.root.set_left(BinaryTreeNode(5))
        self.root.set_right(BinaryTreeNode(9))
        self.tree = BinaryTree(self.root)

    def test_traversals(self):
        strategies = {
            "preorder": (PreOrderTraversal(), [8, 5, 9]),
            "inorder": (InOrderTraversal(), [5, 8, 9]),
            "postorder": (PostOrderTraversal(), [5, 9, 8]),
            "breadth_first": (BreadthFirstTraversal(), [8, 5, 9]),
        }
        for name, (strategy, expected) in strategies.items():
            result = self.tree.traverse(strategy)
            self.assertEqual(result, expected)

    def test_delete_nonexistent(self):
        initial_size = len(self.tree.traverse(InOrderTraversal()))
        self.tree.delete(100)
        new_size = len(self.tree.traverse(InOrderTraversal()))
        self.assertEqual(initial_size, new_size)

    def test_delete_existing(self):
        self.tree.delete(9)
        expected = [5, 8]
        result = self.tree.traverse(InOrderTraversal())
        self.assertEqual(result, expected)
