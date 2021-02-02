def __init__(self, lst = []):
    self.__length = 0
    self.__head = None
    for i in range(len(lst)-1, -1, -1):
        self.add(lst[i])