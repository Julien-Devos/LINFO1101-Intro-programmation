from linked_list import LinkedList

class OrderedLinkedList(LinkedList):

    def __init__(self):
        super().__init__()

    def add(self,cargo):
        """
            cargo: list: liste comprenant le coureur et le temps -> [nom,temps]
        """
        node = self.Node(cargo, None)
        current_node = self.first()
        if current_node == None:
            self.set_first(node)
        elif current_node.next() == None:
            current_node.set_next(node)
        else:
            if current_node.value()[1] > node.value()[1]:
                node.set_next(current_node)
                self.set_first(node)
            else:
                while current_node.next().value()[1] < node.value()[1]:
                    current_node.next()
                    if current_node == None:
                        break
                node.set_next(current_node.next())
                current_node.set_next(node)
        self.inc_size()

    def get(self,coureur):
        try:
            current_node = self.first()
            while current_node.value()[0] != coureur: #TODO coureur.nom
                current_node = current_node.next()
            return current_node.value()[1]
        except AttributeError:
            print("Il n'y a pas de coureur avec le nom: " + coureur)


l = OrderedLinkedList()
l.add(["A",1])
l.add(["B",3])
l.add(["C",2])
l.print_avec_virgule()

print(l.get("D"))