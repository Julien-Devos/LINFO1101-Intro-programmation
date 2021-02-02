def remove(self, cargo):
    if self.first() is None:  # si liste vide
        return
    elif self.first() is self.last() and self.first().value() == cargo:  # si plus qu'une node restante
        node = self.first()
        self.__first = None
        self.__last = None
        return node
    else:
        node = self.first()
        if node.value() == cargo:  # première node
            n = self.__first
            self.__first = node.next()
            return n
        while node.next() is not self.last() and node.next().value() != cargo:
            node = node.next()
        if node.next() is self.last() and node.next().value() != cargo:
            return
        if node.next() is self.last() and node.next().value() == cargo:
            self.__last = node  # dernière node
        n = node.next()
        node.set_next(node.next().next())
        return n


def removeAll(self, cargo):
    if self.first() is None:  # si liste vide
        return
    elif self.first() is self.last() and self.first().value() == cargo:  # si plus qu'une node restante
        node = self.first()
        self.__first = None
        self.__last = None
        return node
    else:
        node = self.first()
        while node is not self.__last:
            if node.value() == cargo:  # première node
                n = self.__first
                self.__first = node.next()
                pass
            while node.next() is not self.last() and node.next().value() != cargo:
                node = node.next()
            if node.next() is self.last() and node.next().value() != cargo:
                pass
            if node.next() is self.last() and node.next().value() == cargo:
                self.__last = node  # dernière node
            n = node.next()
            node.set_next(node.next().next())