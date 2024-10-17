import unittest

from solution import Solution


class MyTestCase(unittest.TestCase):
    def test_algo(self):
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
            self.assertEqual(Solution().infix_to_postfix(expr), expected)

    def test_invalid_string(self):
        self.assertRaises(
            AssertionError, Solution().infix_to_postfix, "(1 + ((2)) /) 52)"
        )
        self.assertRaises(AssertionError, Solution().infix_to_postfix, ")(")
