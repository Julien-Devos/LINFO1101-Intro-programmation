class Employe:

    def __init__(self, n, s):
        self.nom = n
        self.salaire = s

    def augmente(self, amount):
        self.salaire += (amount / 100) * self.salaire

    def __str__(self):
        return "{} : {}".format(self.nom, self.salaire)