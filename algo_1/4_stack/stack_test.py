import unittest
from stack_main import Stack


# class TestStack(unittest.TestCase):
#     def setUp(self) -> None:
#         pass
#
#     def test_size(self):
#         stack = Stack()
#         stack.push(1)
#         stack.push(2)
#         stack.push(3)
#
#         self.assertEqual(stack.size(), 3)
#         self.assertEqual(stack.stack, [1, 2, 3])
#
#     def test_pop(self):
#         stack = Stack()
#         stack.push(1)
#         stack.push(2)
#         stack.push(3)
#         a = stack.pop()
#
#         self.assertEqual(stack.size(), 2)
#         self.assertEqual(stack.stack, [1, 2])
#         self.assertEqual(a, 3)
#
#     def test_pop_empty_stack(self):
#         stack = Stack()
#         a = stack.pop()
#
#         self.assertEqual(stack.size(), 0)
#         self.assertEqual(stack.stack, [])
#         self.assertEqual(a, None)
#
#     def test_pop_one_element(self):
#         stack = Stack()
#         stack.push(1)
#         a = stack.pop()
#
#         self.assertEqual(stack.size(), 0)
#         self.assertEqual(stack.stack, [])
#         self.assertEqual(a, 1)
#
#     def test_push(self):
#         stack = Stack()
#         stack.push(1)
#         stack.push(2)
#         stack.push(3)
#
#         self.assertEqual(stack.size(), 3)
#         self.assertEqual(stack.stack, [1, 2, 3])
#
#     def test_peek(self):
#         stack = Stack()
#         stack.push(1)
#         stack.push(2)
#         stack.push(3)
#
#         a = stack.peek()
#
#         self.assertEqual(stack.size(), 3)
#         self.assertEqual(stack.stack, [1, 2, 3])
#         self.assertEqual(a, 3)


class TestStackViceVersa(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_size(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.stack, [3, 2, 1])

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        a = stack.pop()

        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.stack, [2, 1])
        self.assertEqual(a, 3)

    def test_pop_empty_stack(self):
        stack = Stack()
        a = stack.pop()

        self.assertEqual(stack.size(), 0)
        self.assertEqual(stack.stack, [])
        self.assertEqual(a, None)

    def test_pop_one_element(self):
        stack = Stack()
        stack.push(1)
        a = stack.pop()

        self.assertEqual(stack.size(), 0)
        self.assertEqual(stack.stack, [])
        self.assertEqual(a, 1)

    def test_push(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.stack, [3, 2, 1])

    def test_peek(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        a = stack.peek()

        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.stack, [3, 2, 1])
        self.assertEqual(a, 3)


def is_brackets_balanced(seq: str) -> bool:
    stack = []
    for c in seq:
        if c == '(':
            stack.append(c)
        else:
            if stack and stack[-1] != c:
                stack.pop()
            else:
                return False
    return len(stack) == 0



if __name__ == "__main__":
    unittest.main()

    # print(is_brackets_balanced('()()()'))
    # print(is_brackets_balanced('((()))'))
    # print(is_brackets_balanced(seq="(((())()))"))
    # print(is_brackets_balanced(seq="(()()(()"))
    # print(is_brackets_balanced('))(('))