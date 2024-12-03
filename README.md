# Shunting Yard Algorithm Implementation

[![Tests Status](https://github.com/m4tveevm/etu_algo_labs/actions/workflows/ci.yml/badge.svg)](https://github.com/m4tveevm/etu_algo_labs/actions)
[![Tests Status](https://github.com/m4tveevm/etu_algo_labs/actions/workflows/qodana_code_quality.yml/badge.svg)](https://github.com/m4tveevm/etu_algo_labs/actions)

This project provides an implementation of the **Shunting Yard algorithm**, which converts infix expressions to postfix notation (Reverse Polish Notation). The algorithm was developed by Edsger Dijkstra and is a popular method for parsing mathematical expressions.

## Algorithm Description

The Shunting Yard algorithm processes an input expression in infix notation and outputs it in postfix notation. It uses two main data structures:
- A **stack** to hold operators and parentheses.
- A **queue** to hold the final output in postfix order.

### How It Works

1. Read the expression from left to right.
2. If the token is an operand (number), add it to the output queue.
3. If the token is an operator, pop operators from the stack to the output queue until the top of the stack has an operator of less precedence. Push the current operator onto the stack.
4. If the token is a left parenthesis `(`, push it onto the stack.
5. If the token is a right parenthesis `)`, pop from the stack to the output queue until a left parenthesis is at the top of the stack. Pop the left parenthesis from the stack but do not add it to the output queue.
6. At the end of the expression, pop all operators from the stack to the output queue.

### Example

For the expression `3 + 4 * 5`, the Shunting Yard algorithm will produce the postfix notation: `3 4 5 * +`.

### Visualization

![Shunting Yard Algorithm](https://ucarecdn.com/e7c32a19-818b-48bc-9133-08a1380e6286/)

### Video Demonstration

For a visual demonstration of the algorithm, check out the following video: [Shunting Yard Algorithm Explained](https://www.youtube.com/watch?v=gHniHE_HvhM).

## Implementation

The core implementation is contained within the `Solution` class. Here’s a brief overview of the code:

```python
from src.algo import Queue
from src.algo import Stack


class Solution:
    def __init__(self):
        self.__stack = Stack()
        self.__queue = Queue()

    @staticmethod
    def get_priority(elem):
        return {"+": 0, "-": 0, "*": 1, "/": 1, "^": 2}.get(elem, -1)

    def infix_to_postfix(self, line: str):
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
```

## Test Results

All tests have passed, including:
- Unit tests for the basic classes (Stack and Queue).
- Functionality tests for the Shunting Yard algorithm using predetermined examples.

## Contributing

We welcome contributions to this project! If you have suggestions, improvements, or fixes, feel free to submit a pull request or [open an issue](https://github.com/m4tveevm/etu_algo_labs/issues).

## License

This project is open-source and available under the [MIT License](LICENSE).
