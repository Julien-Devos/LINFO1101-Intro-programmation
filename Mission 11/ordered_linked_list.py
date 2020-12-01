from linked_list import LinkedList
from coureur import Coureur
from resultat import Resultat
from temps import Temps

class OrderedLinkedList(LinkedList):

    def __init__(self):
        super().__init__()

    def add(self,resultat):
        """
            cargo: list: liste comprenant le coureur et le temps -> [nom,temps]
        """
        node = self.Node((resultat.coureur().nom(),resultat), None)
        current_node = self.first()
        if current_node is None:
            self.set_first(node)
        elif current_node.next() is None:
            current_node.set_next(node)
        else:
            if current_node.value()[1] > node.value()[1]:
                node.set_next(current_node)
                self.set_first(node)
            else:
                while current_node.next().value()[1] <= node.value()[1]:
                    current_node = current_node.next()
                    if current_node is None or current_node.next() is None:
                        break
                node.set_next(current_node.next())
                current_node.set_next(node)
        self.inc_size()

    def get(self,coureur):
        try:
            current_node = self.first()
            while current_node.value()[0] != coureur.nom():
                current_node = current_node.next()
            return current_node.value()[1]
        except AttributeError:
            return None

    def get_position(self,coureur):
        try:
            count = 1
            current_node = self.first()
            while current_node.value()[0] != coureur.nom():
                current_node = current_node.next()
                count += 1
            return count
        except AttributeError:
            return -1

    def remove(self,coureur):
        try:
            last_node = None
            current_node = self.first()
            if current_node.value()[0] == coureur.nom():
                super().remove()
            else:
                while current_node.value()[0] != coureur.nom():
                    last_node = current_node
                    current_node = current_node.next()
                last_node.set_next(current_node.next())
                return coureur
        except AttributeError:
            return False

if __name__ == '__main__':
    l = OrderedLinkedList()
    a = Coureur("A",10)
    b = Coureur("B",10)
    c = Coureur("C",10)
    d = Coureur("d",10)
    at = Temps(0, 1, 0)
    bt = Temps(0, 3, 0)
    ct = Temps(0, 2, 0)
    dt = Temps(0, 1, 0)
    l.add(Resultat(a,at))
    l.add(Resultat(b,bt))
    l.add(Resultat(c,ct))
    l.print_avec_virgule()

    print(l.get_position(a))
    print(l.get_position(b))
    print(l.get_position(c))
    l.remove(d)
    l.print_avec_virgule()