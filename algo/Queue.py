from copy import copy
from dataclasses import dataclass


@dataclass
class QueueNode(object):
    data: int = None
    next: object = None
    prev: object = None


class Queue(object):
    def __init__(self):
        self._head = QueueNode()
        self._tail = QueueNode()
        self._head.next = self._tail
        self._tail.prev = self._head
        self.__size = 0

    def __len__(self):
        return copy(self.__size)

    def push(self, value):
        new_node = QueueNode(value)
        new_node.next = self._head.next
        new_node.prev = self._head
        self._head.next.prev = new_node
        self._head.next = new_node
        self.__size += 1

    def pop(self):
        if self._head.next == self._tail:
            return
        pop_result = self._tail.prev
        self._tail.prev = pop_result.prev
        pop_result.prev.next = pop_result.next
        pop_result.next = None
        pop_result.prev = None
        self.__size -= 1
        return pop_result.data
