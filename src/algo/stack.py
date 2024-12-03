from copy import copy
from dataclasses import dataclass


@dataclass
class StackNode(object):
    data: int
    next: object = None


class Stack(object):
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    @property
    def top(self):
        return copy(self._top)

    def push(self, data):
        new_node = StackNode(data)
        self._size += 1
        if not self._top:
            self._top = new_node
            return None
        new_node.next = self._top
        self._top = new_node

    def pop(self):
        if not self._top:
            return None
        self._size -= 1
        top = self._top
        if self._top.next:
            self._top = self._top.next
        else:
            self._top = None
        return top.data
