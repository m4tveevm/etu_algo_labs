from .traversal import TraversalStrategy


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def traverse(self, strategy: TraversalStrategy):
        return strategy.traverse(self.root)

    def delete(self, value):
        self.root = self._delete_rec(self.root, value)

    def _delete_rec(self, node, value):
        if node is None:
            return None
        if value < node.get_value():
            node.set_left(self._delete_rec(node.get_left(), value))
        elif value > node.get_value():
            node.set_right(self._delete_rec(node.get_right(), value))
        else:
            if node.get_left() is None:
                return node.get_right()
            elif node.get_right() is None:
                return node.get_left()
            temp = self._min_value_node(node.get_right())
            node.set_value(temp.get_value())
            node.set_right(
                self._delete_rec(node.get_right(), temp.get_value())
            )
        return node

    @staticmethod
    def _min_value_node(node):
        current = node
        while current.get_left() is not None:
            current = current.get_left()
        return current
