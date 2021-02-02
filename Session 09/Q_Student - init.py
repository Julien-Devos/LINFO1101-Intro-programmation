class Student:
    __next_noma = 0

    def __init__(self, f, s, b, e):
        self.firstname = f
        self.surname = s
        self.birthday = b
        self.email = e
        self.noma = Student.__next_noma
        Student.__next_noma += 1

    def __str__(self):
        return "L'étudiant numéro {} : {} {} né le {}, peut être contacté par {}".format(self.noma, self.firstname,
                                                                                         self.surname, self.birthday,
                                                                                         self.email)