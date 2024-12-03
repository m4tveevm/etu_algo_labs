import unittest

from src.tree.parser import TreeParser


class TestTreeParser(unittest.TestCase):
    def test_correct_parsing(self):
        notation = "(8 (9 (5)) (1))"
        parser = TreeParser(notation)
        root = parser.parse()
        self.assertEqual(root.get_value(), "8")
        self.assertEqual(root.get_left().get_value(), "9")
        self.assertEqual(root.get_right().get_value(), "1")
        self.assertEqual(root.get_left().get_left().get_value(), "5")

    def test_incorrect_parsing(self):
        notation = "(8 (9 (5) (1)"
        parser = TreeParser(notation)
        with self.assertRaises(Exception):
            parser.parse()

        notation = "(8 (9 (5)) (1) extra)"
        parser = TreeParser(notation)
        with self.assertRaises(Exception):
            parser.parse()

    def test_empty_input(self):
        notation = ""
        parser = TreeParser(notation)
        root = parser.parse()
        self.assertIsNone(root)

    def test_complex_tree_parsing(self):
        notation = "(1 (2 (4) (5)) (3 (6) (7)))"
        parser = TreeParser(notation)
        root = parser.parse()
        self.assertEqual(root.get_value(), "1")
        self.assertEqual(root.get_left().get_value(), "2")
        self.assertEqual(root.get_right().get_value(), "3")
        self.assertEqual(root.get_left().get_left().get_value(), "4")
        self.assertEqual(root.get_left().get_right().get_value(), "5")
        self.assertEqual(root.get_right().get_left().get_value(), "6")
        self.assertEqual(root.get_right().get_right().get_value(), "7")
