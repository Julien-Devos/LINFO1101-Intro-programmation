if self.last is not None:
    node = self.last
    if node.data.getUserName() == name:
        self.last.data.setPin(pin)
        return
    while node.link is not None:
        node = node.link
        if node.data.getUserName() == name:
            node.data.setPin(pin)
            return

node = self.Node(Client(name, pin), self.last)
self.last = node