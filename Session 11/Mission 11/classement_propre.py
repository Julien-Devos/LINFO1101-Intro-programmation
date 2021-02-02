#not better solution but 100% on INGInious

from coureur import Coureur
from resultat import Resultat
from temps import Temps

####################
# LinkedList class #
####################

class LinkedList:

    def __init__(self, lst=[]):
        """
        Initialises a new linked list object, with a given list of elements lst.
        @pre:  -
        @post: A new linked list object has been initialised.
               Its length is equal to the number of elements in lst.
               The data elements stored in the linked list's nodes correspond to those of the list lst,
               and appear in the same order as in that list.
               If no list lst is passed as argument, the newly created linked list
               will have 0 length, contain no nodes and its head will point to None.
        """
        self.__length = 0  # current length of the linked list
        self.__head = None  # pointer to the first node in the list
        self.__last = None  # pointer to the last node in the list
        lst.reverse()  # reverse to ensure elements will appear in same order
        for e in lst:  # add elements of input.txt list lst one by one
            self.add(e)

    def size(self):
        """
        Accessor method which returns the number of nodes contained in this linked list.
        @pre:  -
        @post: Returns the number of nodes (possibly zero) contained in this linked list.
        """
        return self.__length

    def inc_size(self):
        """
        Mutator method to increase the size count of this linked list by one.
        @pre:  -
        @post: 1 has been added to the size counter of the number of nodes contained in this linked list.
        """
        self.__length += 1

    def dec_size(self):
        """
        Mutator method to decrease the size count of this linked list by one.
        @pre:  -
        @post: 1 has been substracted from the size counter of the number of nodes contained in this linked list.
        """
        self.__length -= 1

    def first(self):
        """
        Accessor method which returns the first node of this linked list.
        @pre:  -
        @post: Returns a reference to the head of this linked list,
               or None if the linked list contains no nodes.
        """
        return self.__head

    def set_first(self, n):
        """
        Mutator method to reassign the head of this linked list to a new node.
        @pre:  -
        @post: The head of this linked list new refers to node n.
        """
        self.__head = n

    def add(self, cargo):
        """
        Adds a new Node with given cargo to the front of this linked list.
        @pre:  self is a (possibly empty) LinkedList.
        @post: A new Node object is created with the given cargo.
               This new Node is added to the front of the linked list.
               The length counter has been incremented by 1.
               The head of the linked list now points to this new node.
        """
        node = self.Node(cargo, self.first())
        if self.first() == None:  # when this is the first element being added,
            self.__last = node  # set the last pointer to this new node
        self.set_first(node)
        self.inc_size()

    def print(self):
        """
        Prints the contents of this linked list and its nodes.
        @pre:  self is a (possibly empty) LinkedList
        @post: Has printed a space-separated list of the form "[ a b c ... ]",
               where "a", "b", "c", ... are the string representation of each
               of the linked list's nodes.
               A space is printed after and before the opening and closing bracket,
               as well as between any two elements.
               An empty linked is printed as "[ ]".
        """
        self.print_avec_separateur()

    def print_avec_separateur(self, separateur=" "):
        """
        Auxiliary method to print the elements of this linked list,
        separated by a given separateur (by default: a space " ")
        """
        print("[", end=" ")
        if self.first() is not None:
            self.first().print_list_avec_separateur(separateur)
        print("]")

    def print_avec_virgule(self):
        """
        Method to print the elements of this linked list,
        separated by commas and a space: ", ".
        """
        self.print_avec_separateur(", ")

    def print_backward(self):
        """
        Prints the contents of this linked list and its nodes, back to front.
        @pre:  self is a (possibly empty) LinkedList.
        @post: Has printed a space-separated list of the form "[ ... c b a ]",
               where "a", "b", "c", ... are the string representation of each
               of the linked list's nodes. The nodes are printed in opposite order:
               the last nodes' value are printed first.
               A space is printed after and before the opening and closing bracket,
               as well as between any two elements.
               An empty linked is printed as "[ ]".
        """
        print("[", end=" ")
        if self.first() is not None:
            self.first().print_backward()
        print("]")

    def remove(self):
        """
        Removes the node at the start of the list. Leaves the list intact if already empty.
        """
        if self.first() is not None:
            self.dec_size()
            self.set_first(self.first().next())
        if self.size() == 0:  # when there are no more elements in the list,
            self.__last = None  # remove the pointer to the last element

    def add_to_end(self, cargo):
        """
        Adds a node with given cargo to the end of this linked list.
        """
        if self.size() == 0:  # si la liste est encore vide,
            self.add(cargo)  # ajouter Ã  la fin correspond au ajouter au dÃ©but
        else:  # si la liste contient dÃ©jÃ  au moins un noeud (et donc une dernier noeud)
            node = self.Node(cargo)
            self.__last.set_next(node)  # make the current last node point to this new node
            self.__last = node  # set the last node reference to this new node
            self.inc_size()  # increment list size by one

    ##############
    # Node class #
    ##############

    class Node:

        def __init__(self, cargo=None, next=None):
            """
            Initialises a new Node object.
            @pre:  -
            @post: A new Node object has been initialised.
                   A node can contain a cargo and a reference to another node.
                   If none of these are given, the node is initialised with
                   empty cargo (None) and no reference (None).
            """
            self.__cargo = cargo
            self.__next = next

        def value(self):
            """
            Returns the value of the cargo contained in this node.
            @pre:  -
            @post: Returns the value of the cargo contained in this node,
                   or None if no cargo  was put there.
            """
            return self.__cargo

        def next(self):
            """
            Returns the next node to which this node links.
            @pre:  -
            @post: Returns the node to which this node is linked with its
                   next pointer, or None if that pointer is None.
            """
            return self.__next

        def set_next(self, node):
            """
            Sets the next node to which this node links to a new node.
            @pre:  -
            @post: The node to which this node is linked next,
                has been set to the new node passed as parameter.
                   Can also be set to None by passing None as parameter.
            """
            self.__next = node

        def __str__(self):
            """
            Returns a string representation of the cargo of this node.
            @pre:  self is a (possibly empty) Node object.
            @post: Returns a print representation of the cargo contained in this Node.
            """
            return str(self.value())

        def __eq__(self, other):
            """
            Comparator to compare two Node objects by their cargo.
            """
            if other is not None:
                return self.value() == other.value()
            else:
                return False

        def print_list(self):
            """
            Prints the cargo of this node and then recursively of each node connected to this one.
            @pre:  self is a node (possibly connected to a next node).
            @post: Has printed a space-separated list of the form "a b c ... ",
                   where "a" is the string-representation of this node,
                   "b" is the string-representation of my next node, and so on.
                   A space is printed in-between the printed value.
            """
            head = self
            tail = self.__next  # go to my next node
            if tail is not None:  # as long as the end of the list has not been reached
                print(head, end=" ")  # print my head
                tail.print_list()  # recursively print remainder of the list
            else:  # print the last element
                print(head, end=" ")

        def print_backward(self):
            """
            Recursively prints the cargo of each node connected to this node (in opposite order),
            and then prints the cargo of this node as last value.
            @pre:  self is a node (possibly connected to a next node).
            @post: Has printed a space-separated list of the form "... c b a",
                   where a is my cargo (self), b is the cargo of the next node, and so on.
                   The nodes are printed in opposite order: the last nodes' value is printed first.
            """
            head = self
            tail = self.__next  # go to my next node
            if tail is not None:  # as long as the end of the list has not been reached
                tail.print_backward()  # recursively print remainder of the list backwards
            print(head, end=" ")  # print my head

        def print_avec_separateur(self, separateur):
            print("[", end=" ")
            if self.first() is not None:
                self.head.print_list_avec_separateur(separateur)
            print("]")

        def print_list_avec_separateur(self, separateur):
            head = self
            tail = self.__next  # go to my next node
            if tail is not None:  # as long as the end of the list has not been reached
                print(head, end=separateur)  # print my head, with separateur
                tail.print_list_avec_separateur(separateur)  # recursively print remainder of the list
            else:  # print the last element
                print(head, end=" ")  # print my head, with a space

class OrderedLinkedList(LinkedList):

    def __init__(self):
        """ Initialise un objet de type OrderedLinkedList en appellant la classe mère LinkedList """
        super().__init__()

    def add(self,resultat):
        """ Permet d'ajouter un Résultat dans la liste ordonée OrderedLinkedList

            Args:
                resultat: Resultat: un objet de type Resultat
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
        """ Permet d'obtenir le résultat d'un Coureur dans la liste ordonée OrderedLinkedList

            Args:
                coureur: Coureur: un objet de type Coureur

            Returns:
                le Résultat du coureur Coureur si il se trouve dans la liste et None si non
        """
        try:
            current_node = self.first()
            while current_node.value()[0] != coureur.nom():
                current_node = current_node.next()
            return current_node.value()[1]
        except AttributeError:
            return None

    def get_position(self,coureur):
        """ Permet d'obtenir la position d'un coureur Coureur dans la liste ordonée OrderedLinkedList

            Args:
                coureur: Coureur: un pbjet de type Coureur

            Returns:
                la position si le coureur Coureur se trouve dans le liste et -1 si non
        """
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
        """ Permet de supprimer un coureur Coureur dans la liste ordonée OrderedLinkedList

            Args:
                coureur: Coureur: un objet de type Coureur

            Returns:
                l'objet Coureur si il est présent dans la liste et False si non
        """
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

class Classement :
    """
    Une implémentation primitive de classement, non ordonnée et de capacité fixe.
    @author Kim Mens
    @version 01 Décembre 2019
    """

    __maxcapacity = 10

    def __init__(self):
        """
        @pre: -
        @post: un classement vide de taille 0 a été créé
        """
        self.__resultats = OrderedLinkedList()   # liste chainée ordonnée
        self.__size = 0         # nombre de résultats actuel (initialement 0, maximum __maxcapacity)

    def size(self):
        """
        Méthode accesseur.
        Retourne la taille de ce classement.
        @pre:  -
        @post: Le nombre de résultats actuellement stockés dans ce classement a été retourné.
        """
        return self.__size

    def add(self,r):
        """
        Ajoute un résultat r dans ce classement.
        @pre:  r est une instance de la classe Resultat
        @post: Le résultat r a été inséré selon l'ordre du classement.
               En cas d'ex-aequo, r est inséré après les autres résultats de même ordre.
        ATTENTION : L'implémentation actuelle ne respecte pas encore la post-condition!
                    Le résultat est simplement ajouté Ã  la dictionnaire, sans tenir compte de l'ordre.
                    Une dictionnaire ne donne pas de garanties sur l'ordre des éléments.
        """
        if self.size() >= self.__maxcapacity :
            # DONT WORK raise Error("Capacity of classement exceeded")
            return False
        else :
            self.__size += 1
            self.__resultats.add(r)

    def get(self,c):
        """
        Retourne le résultat d'un coureur donné.
        @pre c est un Coureur
        @post retourne le premier (meilleur) Resultat r du coureur c dans le
              classement. Retourne None si le coureur ne figure pas (encore)
              dans le classement.
        """
        return self.__resultats.get(c)

    def get_position(self,c):
        """
        Retourne la meilleure position d'un coureur dans ce classement.
        @pre c est un Coureur
        @post retourne un entier représentant la position du coureur c dans ce classement,
              Ã  partir de 1 pour la tête de ce classement. Si le coureur figure plusieurs fois
              dans le classement, la première (meilleure) position est retournée.
              Retourne -1 si le coureur ne figure pas dans le classement.
        ATTENTION : L'implémentation actuelle ne respecte pas encore la post-condition!
                    Etant donné que la dictionnaire de résultats ne connaÃ®t pas de position,
                    pour le moment cette méthode retourne toujours "***position inconnue***".
                    A vous de la corriger en utilisant une liste chaÃ®née ordonnée
                    comme structure de données, plutÃ´t qu'une simple dictionnaire.
        """
        return self.__resultats.get_position(c)

    def remove(self,c):
        """
        Retire un résultat du classement.
        @pre  c est un Coureur
        @post retire le premier (meilleur) résultat pour le coureur c du classement.
              c est comparé au sens de __eq__. Retourne c si un résultat a été retiré,
              of False si c n'est pas trouvé dans la liste.
        """
        self.__size -= 1
        return self.__resultats.remove(c)

    def __str__(self):
        """
        Méthode magique
        Retourne une représentation string de cet objet.
        @pre:  -
        @post: Retourne une représentation de ce classement sous forme d'un string,
               avec une ligne par résultat.
        """
        s = ""
        d = self.__resultats.first()
        if d is None:
            s += "  " + str(self.get_position(d.value()[0])) + " > " + str(d.value()[1]) + "\n"
        else:
            while d.value() is not None:
                s += "  " + str(self.get_position(d.value()[0])) + " > " + str(d.value()[1]) + "\n"
                d = d.next()
                if d is None:
                    break
        return s