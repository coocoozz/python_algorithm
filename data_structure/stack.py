class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            value = self.stack[-1]
            del self.stack[-1]
            return value
        else:
            return None

    def size(self):
        return len(self.stack)

    def empty(self):
        if self.stack:
            return False
        else:
            return True

    def top(self):
        if self.empty():
            return None
        else:
            return self.stack[self.size() - 1]

    def clear(self):
        self.stack.clear()

