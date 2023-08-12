class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        """Complexity O(1), but memory reallocation takes more time -> o(1)."""
        if self.size():
            first = self.stack[0]
            self.stack = self.stack[1:]
            return first
        return None

    def push(self, value):
        """Complexity O(n) because we need to shift the elements on 1 position to the right"""
        self.stack = [value] + self.stack

    def peek(self):
        if self.size():
            return self.stack[0]
        return None
