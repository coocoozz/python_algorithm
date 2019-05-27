class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        if self.stack:
            val = self.stack[-1]
            del self.stack[-1]
            return val
        else:
            return -1

    def size(self):
        return len(self.stack)

    def empty(self):
        if self.stack:
            return 0
        else:
            return 1

    def top(self):
        if self.empty():
            return -1
        else:
            return self.stack[self.size() - 1]

