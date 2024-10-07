import unittest

from .Queue import Queue
from .Stack import Stack


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_push_and_pop(self):
        self.queue.push(1)
        self.queue.push(2)
        self.queue.push(3)
        self.assertEqual(len(self.queue), 3)
        self.assertEqual(self.queue.pop(), 1)
        self.assertEqual(self.queue.pop(), 2)
        self.assertEqual(self.queue.pop(), 3)
        self.assertIsNone(self.queue.pop())

    def test_pop_empty(self):
        self.assertIsNone(self.queue.pop())

    def test_len_empty(self):
        self.assertEqual(len(self.queue), 0)


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push_and_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(len(self.stack), 3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertIsNone(self.stack.pop())

    def test_pop_empty(self):
        self.assertIsNone(self.stack.pop())

    def test_len_empty(self):
        self.assertEqual(len(self.stack), 0)


if __name__ == "__main__":
    unittest.main()
