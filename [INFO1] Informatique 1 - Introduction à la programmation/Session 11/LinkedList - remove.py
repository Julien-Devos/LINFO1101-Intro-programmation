def remove(self):
    if self.__length > 0:
        self.__head = self.__head.next()
        self.__length -= 1