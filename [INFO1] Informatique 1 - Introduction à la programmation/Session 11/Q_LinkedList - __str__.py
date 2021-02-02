def __str__(self):
    node = self.first()
    if node == None:
        return "[ ]"
    s = "[ "
    while node.next() is not None:
        s += str(node.value()) + " "
        node = node.next()

    s += str(node.value()) + " ]"
    return s