class CD(Item):
    __serial = 100000
    def __init__(self,author,title,duree):
        super().__init__(author,title,CD.__serial)
        self.duree = duree
        CD.__serial += 1
    def __str__(self):
        s = super().__str__()
        return s + " ({} s)".format(self.duree)