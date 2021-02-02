class Node:
    def __init__(self, s=None, prev=None, next=None):
        self.value = s
        self.previous = prev
        self.next = next

    def get_text(self):
        return str(self.value)

    def set_text(self, s):
        self.value = s

#*********************************************

class Tape:
    def __init__(self):
        self.len = 0
        self.head = None
        self.last = None
        self.curr = None

    def add(self, s):
        node = Node(s, self.last)
        if self.len == 0:
            self.head = node
            self.curr = node
        elif self.last is not None:
            self.last.next = node
        self.last = node
        self.len += 1

    def next(self):
        if self.curr.next is not None:
            self.curr = self.curr.next
            return self.curr.value
        return None

    def previous(self):
        if self.curr.previous is not None:
            self.curr = self.curr.previous
            return self.curr.value
        return None

    def get_length(self):
        return self.len

    def write(self, s):
        if self.curr is not None:
            self.curr.set_text(s)

    def read(self):
        if self.curr is not None:
            return self.curr.get_text()
        return None
