import unittest

from solution import Solution


class MyTestCase(unittest.TestCase):
    def setup(self):
        self.__sol = Solution()

    def test_algo(self):
        self.setup()
        test_cases = [
            ("3 + 4 * 5", ["3", "4", "5", "*", "+"]),
            ("( 3 + 4 ) * 5", ["3", "4", "+", "5", "*"]),
            ("2 * 3 * 4 / 2", ["2", "3", "*", "4", "*", "2", "/"]),
            ("6 / 2 * 3", ["6", "2", "/", "3", "*"]),
            ("2 * 3 ^ 4", ["2", "3", "4", "^", "*"]),
            ("10 - 3 + 5", ["10", "3", "-", "5", "+"]),
            ("2 * ( 3 + ( 4 * 5 ) )", ["2", "3", "4", "5", "*", "+", "*"]),
            (
                "3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3",
                ["3", "4", "2", "*", "1", "5", "-", "2", "^", "3", "^", "/", "+"],
            ),
            ("5", ["5"]),
            ("+", ["+"]),
            ("( 7 + 3 ) * ( 5 - 2 )", ["7", "3", "+", "5", "2", "-", "*"]),
            ("-3 + 2", ["2", "+", "-3"]),
            (
                "3 * ( 4 + ( 5 - 2 ) / ( 2 * 3 ) )",
                ["3", "4", "5", "2", "-", "2", "3", "*", "/", "+", "*"],
            ),
            (
                "2 + 3 - 4 * 5 / 6 ^ 7",
                ["2", "3", "+", "4", "5", "*", "6", "7", "^", "/", "-"],
            ),
            ("6 * 2 / 3", ["6", "2", "*", "3", "/"]),
            ("2 ^ 3 ^ 4", ["2", "3", "^", "4", "^"]),
            ("4 + -5 * 6", ["4", "+", "6", "*", "-5"]),
            (
                "1 + 2 - 3 * 4 / 5 ^ 6",
                ["1", "2", "+", "3", "4", "*", "5", "6", "^", "/", "-"],
            ),
            ("", []),
        ]

        for expr, expected in test_cases:
            self.assertEqual(self.__sol.infix_to_postfix(expr), expected)
