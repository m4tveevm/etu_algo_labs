from abc import ABC, abstractmethod


class TreeNode(ABC):
    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def set_value(self, value):
        pass

    @abstractmethod
    def get_left(self):
        pass

    @abstractmethod
    def get_right(self):
        pass

    @abstractmethod
    def set_left(self, node):
        pass

    @abstractmethod
    def set_right(self, node):
        pass


class BinaryTreeNode(TreeNode):
    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    def get_left(self):
        return self._left

    def get_right(self):
        return self._right

    def set_left(self, node):
        self._left = node

    def set_right(self, node):
        self._right = node
