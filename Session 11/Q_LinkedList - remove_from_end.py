def remove_from_end(self):
    n = self.__head
    if self.__head is not None:
        if n.next() is None:
            self.__head = None
        else:
            while n.next().next() is not None:
                n = n.next()
            n.set_next(None)
        self.__length -= 1
