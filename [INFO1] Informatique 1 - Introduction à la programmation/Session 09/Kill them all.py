class Character:
    def __init__(self, l, a):
        self.life = l
        self.attack_point = a

    def attack(self, target):
        target.life -= self.attack_point

    def get_hit(self, damage):
        self.life -= damage


class Cratos(Character):
    def __init__(self):
        super().__init__(100, 10)
        self.experience = 0

    def gain_XP(self, amount):
        self.experience += amount
        while self.experience >= 10:
            self.attack_point += 1
            self.experience -= 10


class Drauf(Character):
    def __init__(self, life, attack_point):
        super().__init__(life, attack_point)