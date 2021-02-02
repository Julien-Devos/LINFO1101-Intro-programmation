def insert(self, s):
    element = self.first()
    if element is None:
        self.add(s)
    elif element.value() > s:
        self.__head = self.Node(s, self.__head)
    else:
        if element.next() is not None:
            while s > element.next().value():
                element = element.next()
                if element.next() is None:
                    break
        element.set_next(self.Node(s, element.next()))
    self.__length += 1