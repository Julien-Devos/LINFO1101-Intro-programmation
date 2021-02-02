class Command:
    __commands = 0
    __tot_p = 0

    @classmethod
    def get_number_total_command(cls):
        return cls.__commands

    @classmethod
    def get_total_price(cls):
        return cls.__tot_p

    def __init__(self, id_b, id_i, q, p):
        self.id_buyer = id_b
        self.id_item = id_i
        self.quantity_item = q
        self.price_item = p
        Command.__commands += 1
        Command.__tot_p += self.get_price()

    def get_price(self):
        return self.price_item * self.quantity_item

    def __str__(self):
        return F"{self.id_buyer}, {self.id_item} : {self.price_item} * {self.quantity_item} = {self.get_price()}"