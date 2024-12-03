from .nodes import BinaryTreeNode
from .traversal import TraversalStrategy


class RBTreeNode(BinaryTreeNode):
    def __init__(self, value, color="RED"):
        super().__init__(value)
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node


class RedBlackTree:
    def __init__(self):
        self.nil = RBTreeNode(None, color="BLACK")
        self.nil.left = self.nil.right = self.nil
        self.nil.parent = None
        self.root = self.nil

    def insert(self, value):
        new_node = RBTreeNode(value)
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.color = "RED"
        parent = None
        current = self.root

        while current != self.nil:
            parent = current
            if new_node.get_value() < current.get_value():
                current = current.get_left()
            else:
                current = current.get_right()

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.get_value() < parent.get_value():
            parent.set_left(new_node)
        else:
            parent.set_right(new_node)

        self.insert_fixup(new_node)

    def insert_fixup(self, node):
        while node.parent and node.parent.color == "RED":
            if node.parent == node.parent.parent.get_left():
                uncle = node.parent.parent.get_right()
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.get_right():
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.get_left()
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.get_left():
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.left_rotate(node.parent.parent)
        self.root.color = "BLACK"

    def left_rotate(self, x):
        y = x.get_right()
        x.set_right(y.get_left())
        if y.get_left() != self.nil:
            y.get_left().parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.get_left():
            x.parent.set_left(y)
        else:
            x.parent.set_right(y)
        y.set_left(x)
        x.parent = y

    def right_rotate(self, y):
        x = y.get_left()
        y.set_left(x.get_right())
        if x.get_right() != self.nil:
            x.get_right().parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.get_right():
            y.parent.set_right(x)
        else:
            y.parent.set_left(x)
        x.set_right(y)
        y.parent = x

    def search(self, value):
        current = self.root
        while current != self.nil and current.get_value() != value:
            if value < current.get_value():
                current = current.get_left()
            else:
                current = current.get_right()
        return current

    def minimum(self, node):
        while node.get_left() != self.nil:
            node = node.get_left()
        return node

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.get_left():
            u.parent.set_left(v)
        else:
            u.parent.set_right(v)
        v.parent = u.parent

    def delete(self, value):
        node = self.search(value)
        if node == self.nil:
            return False  # Узел не найден

        y = node
        y_original_color = y.color
        if node.get_left() == self.nil:
            x = node.get_right()
            self.transplant(node, node.get_right())
        elif node.get_right() == self.nil:
            x = node.get_left()
            self.transplant(node, node.get_left())
        else:
            y = self.minimum(node.get_right())
            y_original_color = y.color
            x = y.get_right()
            if y.parent == node:
                x.parent = y
            else:
                self.transplant(y, y.get_right())
                y.set_right(node.get_right())
                y.get_right().parent = y
            self.transplant(node, y)
            y.set_left(node.get_left())
            y.get_left().parent = y
            y.color = node.color
        if y_original_color == "BLACK":
            self.delete_fixup(x)
        return True

    def delete_fixup(self, x):
        while x != self.root and x.color == "BLACK":
            if x == x.parent.get_left():
                w = x.parent.get_right()
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.left_rotate(x.parent)
                    w = x.parent.get_right()
                if (
                    w.get_left().color == "BLACK"
                    and w.get_right().color == "BLACK"
                ):
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.get_right().color == "BLACK":
                        w.get_left().color = "BLACK"
                        w.color = "RED"
                        self.right_rotate(w)
                        w = x.parent.get_right()
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.get_right().color = "BLACK"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.get_left()
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.right_rotate(x.parent)
                    w = x.parent.get_left()
                if (
                    w.get_right().color == "BLACK"
                    and w.get_left().color == "BLACK"
                ):
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.get_left().color == "BLACK":
                        w.get_right().color = "BLACK"
                        w.color = "RED"
                        self.left_rotate(w)
                        w = x.parent.get_left()
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.get_left().color = "BLACK"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "BLACK"

    def traverse(self, strategy: TraversalStrategy):
        return strategy.traverse(self.root, self.nil)
