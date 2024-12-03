from abc import ABC, abstractmethod

from src.algo.queue import Queue


class TraversalStrategy(ABC):
    @abstractmethod
    def traverse(self, root, nil=None):
        pass


class PreOrderTraversal(TraversalStrategy):
    def traverse(self, root, nil=None):
        result = []
        stack = []
        if root and root != nil:
            stack.append(root)
        while stack:
            node = stack.pop()
            result.append(node.get_value())
            if node.get_right() and node.get_right() != nil:
                stack.append(node.get_right())
            if node.get_left() and node.get_left() != nil:
                stack.append(node.get_left())
        return result


class InOrderTraversal(TraversalStrategy):
    def traverse(self, root, nil=None):
        result = []
        stack = []
        current = root
        while stack or (current and current != nil):
            if current and current != nil:
                stack.append(current)
                current = current.get_left()
            else:
                current = stack.pop()
                result.append(current.get_value())
                current = current.get_right()
        return result


class PostOrderTraversal(TraversalStrategy):
    def traverse(self, root, nil=None):
        result = []
        stack = []
        last_node_visited = None
        current = root
        while stack or (current and current != nil):
            if current and current != nil:
                stack.append(current)
                current = current.get_left()
            else:
                peek_node = stack[-1]
                if (
                    peek_node.get_right()
                    and last_node_visited != peek_node.get_right()
                    and peek_node.get_right() != nil
                ):
                    current = peek_node.get_right()
                else:
                    result.append(peek_node.get_value())
                    last_node_visited = stack.pop()
                    current = None
        return result


class BreadthFirstTraversal(TraversalStrategy):
    def traverse(self, root, nil=None):
        result = []
        queue = Queue()
        if root and root != nil:
            queue.push(root)
        while queue:
            node = queue.pop()
            result.append(node.get_value())
            if node.get_left() and node.get_left() != nil:
                queue.push(node.get_left())
            if node.get_right() and node.get_right() != nil:
                queue.push(node.get_right())
        return result
