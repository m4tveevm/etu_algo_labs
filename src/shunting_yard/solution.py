from src.algo.line_check import validate_brackets
from src.algo.queue import Queue
from src.algo.stack import Stack


class Solution:
    def __init__(self):
        self.__stack = Stack()
        self.__queue = Queue()

    @staticmethod
    def get_priority(elem):
        return {"+": 0, "-": 0, "*": 1, "/": 1, "^": 2}.get(elem, -1)

    def infix_to_postfix(self, line: str):
        assert validate_brackets(line)
        for elem in line.split():
            if elem.isnumeric():
                self.__queue.push(elem)
            elif elem == "(":
                self.__stack.push(elem)
            elif elem == ")":
                while self.__stack and self.__stack.top.data != "(":
                    self.__queue.push(self.__stack.pop())
                self.__stack.pop()
            else:
                while self.__stack and self.get_priority(
                    self.__stack.top.data
                ) >= self.get_priority(elem):
                    self.__queue.push(self.__stack.pop())
                self.__stack.push(elem)

        while self.__stack:
            self.__queue.push(self.__stack.pop())

        return [self.__queue.pop() for _ in range(len(self.__queue))]
