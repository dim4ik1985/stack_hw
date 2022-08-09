from collections import deque


class MyStack:
    def __init__(self):
        self.my_stack = deque()

    def is_empty(self):
        if self.size() != 0:
            return False
        else:
            return True

    def pop(self):
        if self.size() == 0:
            return None
        return self.my_stack.pop()

    def push(self, item):
        self.my_stack.append(item)

    def peek(self):
        if self.size() == 0:
            return None
        return self.my_stack[0]

    def size(self):
        return len(self.my_stack)

