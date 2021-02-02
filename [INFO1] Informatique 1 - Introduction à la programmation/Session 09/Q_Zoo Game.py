class Animal:
    def __init__(self, name, diurnal=None, nb_legs=None, asleep=False):
        self.name = name
        self.diurnal = diurnal
        self.nb_legs = nb_legs
        self.asleep = asleep

    def sleep(self):
        if self.asleep == False:
            self.asleep = True
        else:
            raise RuntimeError

    def wake_up(self):
        if self.asleep == True:
            self.asleep = False
        else:
            raise RuntimeError


class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, True, 4)

    def roar(self):
        print("ROARRR!!!")


class Owl(Animal):
    def __init__(self, name):
        super().__init__(name, False, 2)

    def fly(self):
        pass


class Giraffe(Animal):
    def __init__(self, name, size):
        super().__init__(name)
        self.diurnal = True
        self.nb_legs = 4
        try:
            float(size)
            if size > 0:
                self.size = size
            else:
                raise ValueError
        except:
            raise ValueError

    def neck_length(self):
        return size


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
        else:
            raise ValueError


def create_my_zoo():
    zoo = Zoo()
    Simba = Lion("Simba")
    Leonie = Giraffe("Léonie", 1)
    Zoe = Giraffe("Zoé", 1)
    Pocahontas = Owl("Pocahontas")
    zoo.add_animal(Leonie)
    zoo.add_animal(Zoe)
    zoo.add_animal(Simba)
    zoo.add_animal(Pocahontas)
    return zoo