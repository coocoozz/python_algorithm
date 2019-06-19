class Deque:
    def __init__(self):
        self.deque = list()

    def push_front(self, val):
        self.deque.insert(0, val)

    def push_back(self, val):
        self.deque.append(val)

    def pop_front(self):
        if self.empty() is True:
            return None
        else:
            return self.deque.pop(0)

    def pop_back(self):
        if self.empty() is True:
            return None
        else:
            return self.deque.pop()

    def size(self):
        return len(self.deque)

    def empty(self):
        if self.size() is 0:
            return True
        else:
            return False

    def front(self):
        if self.empty() is True:
            return None
        else:
            return self.deque[0]

    def back(self):
        if self.empty() is True:
            return None
        else:
            return self.deque[self.size()-1]

