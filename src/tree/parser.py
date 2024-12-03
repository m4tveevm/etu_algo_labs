from .nodes import BinaryTreeNode


class TreeParser:
    def __init__(self, line):
        self.tokens = line.replace("(", " ( ").replace(")", " ) ").split()
        self.index = 0

    def parse(self):
        if self.index >= len(self.tokens):
            return None

        token = self.tokens[self.index]
        if token == "(":
            self.index += 1
            if self.index >= len(self.tokens):
                raise Exception("Ожидалось значение после '('")
            value = self.tokens[self.index]
            self.index += 1
            node = BinaryTreeNode(value)
            node.set_left(self.parse())
            node.set_right(self.parse())
            if (
                self.index >= len(self.tokens)
                or self.tokens[self.index] != ")"
            ):
                raise Exception("Ожидалась ')'")
            self.index += 1
            return node
        elif token == ")":
            return None
        else:
            self.index += 1
            return BinaryTreeNode(token)
