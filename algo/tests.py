import unittest

from .Queue import Queue
from .Stack import Stack

# from .LineCheck import is_valid


class TestQueue(unittest.TestCase):
    def setup(self):
        self.__queue = Queue()

    def test_push_and_pop(self):
        self.setup()
        self.__queue.push(1)
        self.__queue.push(2)
        self.__queue.push(3)
        self.assertEqual(len(self.__queue), 3)
        self.assertEqual(self.__queue.pop(), 1)
        self.assertEqual(self.__queue.pop(), 2)
        self.assertEqual(self.__queue.pop(), 3)
        self.assertIsNone(self.__queue.pop())

    def test_pop_empty(self):
        self.setup()
        self.assertIsNone(self.__queue.pop())

    def test_len_empty(self):
        self.setup()
        self.assertEqual(len(self.__queue), 0)


class TestStack(unittest.TestCase):
    def setup(self):
        self.__stack = Stack()

    def test_push_and_pop(self):
        self.setup()
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.push(3)
        self.assertEqual(len(self.__stack), 3)
        self.assertEqual(self.__stack.pop(), 3)
        self.assertEqual(self.__stack.pop(), 2)
        self.assertEqual(self.__stack.pop(), 1)
        self.assertIsNone(self.__stack.pop())

    def test_pop_empty(self):
        self.setup()
        self.assertIsNone(self.__stack.pop())

    def test_len_empty(self):
        self.setup()
        self.assertEqual(len(self.__stack), 0)


if __name__ == "__main__":
    unittest.main()
