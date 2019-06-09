class Queue:
    def __init__(self):
        self.queue = list()

    def clear(self):
        self.queue.clear()

    def push(self, val):
        self.queue.append(val)

    def pop(self):
        if self.empty() is True:
            return None
        else:
            val = self.queue[0]
            del self.queue[0]
            return val

    def size(self):
        return len(self.queue)

    def empty(self):
        if self.size() is 0:
            return True
        else:
            return False

    def front(self):
        if self.empty() is True:
            return None
        else:
            return self.queue[0]

    def back(self):
        if self.empty() is True:
            return None
        else:
            return self.queue[self.size() - 1]

