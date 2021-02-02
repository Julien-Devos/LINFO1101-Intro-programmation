class LinkedList:
    def __init__(self):
        self.__head = None
        self.__len = 0

    def add(self, cargo):
        node = Node(cargo, self.__head)
        self.__head = node
        self.__len += 1

    def get_reverse(self):
        node = self.__head
        s = node.get_value()
        while node.get_next() is not None:
            node = node.get_next()
            s += node.get_value()
        return s


class Node:
    def __init__(self, cargo=None, next=None):
        self.__next = next
        self.__value = cargo

    def get_next(self):
        return self.__next

    def set_next(self, value):
        self.__next = value

    def get_value(self):
        return str(self.__value)

