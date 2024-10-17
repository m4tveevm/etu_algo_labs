from .Stack import Stack


def is_valid(bracket_sequence):
    stack = Stack()
    brackets_dict = {
        "[": "]",
        "{": "}",
        "(": ")",
    }
    for bracket in bracket_sequence:
        if bracket not in ("[", "{", "(", ")", "}", "]"):
            continue
        if bracket in brackets_dict:
            stack.push(bracket)
        elif len(stack) == 0 or bracket != brackets_dict[stack.pop()]:
            return False
    return len(stack) == 0
