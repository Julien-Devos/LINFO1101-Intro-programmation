"""
    Classes fournies pour la mission 9; à  compléter par les étudiants.
    @author Kim Mens
    @version 8 novembre 2020
"""

###############
### ARTICLE ###
###############

"""
    Cette classe représente un Article de facture simple,
    comprenant un descriptif et un prix.

    @author Kim Mens
    @version 18 novembre 2018
    (code adapté du code java de Charles Pecheur)
"""


class Article:
    __taux_tva = 0.21  # TVA a 21%

    @classmethod
    def getTVA(cls):
        return cls.__taux_tva

    def __init__(self, d, p):
        """
            Cree un article avec description d et prix p.
        """
        self.__description = d
        self.__prix = p

    def description(self):
        """
            Retourne la description de cet article.
        """
        return self.__description

    def prix(self):
        """
            Retourne le prix (HTVA) de cet article.
        """
        return self.__prix

    def taux_tva(self):
        """
            Retourne le taux de TVA (même valeur pour chaque article)
        """
        return Article.getTVA()

    def tva(self):
        """
            Retourne la TVA sur cet article
        """
        return self.prix() * self.taux_tva()

    def prix_tvac(self):
        """
            Retourne le prix de l'article, TVA compris.
        """
        return self.prix() + self.tva()

    def __str__(self):
        """
            Retourne un texte decrivant cet article, au format: "{description}: {prix}"
        """
        return "{0}: {1:.2f}".format(self.description(), self.prix())


###############
### FACTURE ###
###############

"""
    Cette classe représente une Facture, sous forme d'une liste d'articles.

    @author Kim Mens
    @version 18 novembre 2018
    (code adapté du code java de Charles Pecheur)
"""


class Facture:
    __fact_number = 1

    def __init__(self, description, articles):
        """
            Crée une facture avec une description (titre) et une liste d'articles.
            @pre  description est un string court décrivant la facture
                  articles est une liste d'objets de type Article
            @post Une facture avec une description (titre) et un liste d'articles a été créée.
        """
        self.__reference = description
        self.__articles = articles
        self.__number = Facture.__fact_number
        Facture.__fact_number += 1

    def description(self):
        """
            Retourne la description de cette facture.
        """
        return self.__reference

    def articles(self):
        """
            Retourne la liste des articles de cette facture.
        """
        return self.__articles

    def __str__(self):
        """
            Retourne la représentation string d'une facture, à  imprimer avec la méthode print().
        """
        s = self.entete_str()
        totalPrix = 0.0
        totalTVA = 0.0
        for art in self.articles():
            s += self.article_str(art)
            totalPrix = totalPrix + art.prix()
            totalTVA = totalTVA + art.tva()
        s += self.totaux_str(totalPrix, totalTVA)
        return s

    def entete_str(self):
        """
            Imprime l'entête de la facture, comprenant le descriptif et les têtes de colonnes.
        """
        e = "Facture No " + str(self.__number) + " : " + self.description() + "\n"
        e += self.barre_str()
        e += "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description", "prix HTVA", "TVA", "prix TVAC")
        e += self.barre_str()
        return e

    def barre_str(self):
        """
            Retourne un string représentant une barre horizontale sur la largeur de la facture.
        """
        b = ""
        barre_longeur = 83
        for i in range(barre_longeur):
            b += "="
        return b + "\n"

    def article_str(self, art):
        """
            Retourne un string correspondant à  une ligne de facture pour l'article art
        """
        return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(art.description(), art.prix(), art.tva(), art.prix_tvac())

    def totaux_str(self, prix, tva):
        """
            Retourne un string représentant une ligne de facture avec les totaux prix et tva, à  imprimer en bas de la facture
        """
        b = self.barre_str()
        b += "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format("T O T A L", prix, tva, prix + tva)
        b += self.barre_str()
        return b

    # Cette méthode doit être ajoutée lors de l'étape 4 de la mission
    def nombre(self, pce):
        """
            Retourne le nombre d'exemplaires de la Piece pce dans la facture, en totalisant sur tous les articles qui concernent cette pièce.
        """
        count = 0
        for i in self.__articles:
            if i.description() == pce.description():
                count += 1
        return count


    # Cette méthode doit être ajoutée lors de l'étape 5 de la mission
    def livraison_str(self):
        """
            Cette méthode est une méthode auxiliaire pour la méthode printLivraison qui fonctionne quand la liste d'articles est remplie d'instance de ArticlePiece
        """
        e = "Livraison - Facture No " + str(self.__number) + " : " + self.description() + "\n"
        e += self.barre_str()
        e += "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description", "poids/pce", "nombre", "poids")
        e += self.barre_str()
        total_art, total_nbr, total_poids, count = 0, 0, 0, 0
        for art in self.__articles:
            i = ""
            if type(art) == ArticlePiece:
                if art.piece().fragile():
                    count += 1
                    i = " (!)"
                total_art += 1
                total_poids += art.piece().poids()*art.nombre()
                total_nbr += art.nombre()
                e += "| {0:40} | {1:8.3f}kg | {2:10} | {3:8.3f}kg |\n".format(art.piece().description() + i, art.piece().poids(), art.nombre(), art.piece().poids()*art.nombre())
        e += self.barre_str()
        e += "| {0:40} | {1:10} | {2:10} | {3:8.3f}kg |\n".format((str(total_art) + " articles"), "", total_nbr, total_poids)
        e += self.barre_str()
        if count > 0:
            e += " (!) *** livraison fragile ***"
        return e

class ArticleReparation(Article):

    def __init__(self,d):
        """ Crée un objet ArticleRéparation réparé pendant d heures.
            Args:
                d: float: une durée en heure

            Returns:
                 Un objet ArticleReparation avec une durée
        """
        super().__init__("Réparation",20 + 35*d)
        self.__duree = d

    def get_duree(self):
        """
            Retourne la duree de la réparation
        """
        return self.__duree

    def description(self):
        """
            Retourne la description de la réparation.
        """
        return super().description()

    def prix(self):
        """
            Retourne le prix (HTVA) de la réparation.
        """
        return super().prix()

class Piece:

    def __init__(self,d,prix,poids = 0,fragile = False,reduc = False):
        """ Crée un objet Piece qui a comme paramètres une description, un prix, un poids,
            un bool fragile ou non et un bool réduction TVA

            Args:
                d: str: la description de la Piece
                prix: float: le prix de la Piece
                poids: float: le poids de la piece en kg
                fragile: bool: True si fragile et False si non
                reduc: bool: True si en réduc et False si non

            Returns:
                Un objet de type Piece
        """
        self.__description = d
        self.__prix = prix
        self.__poids = poids
        self.__is_fragile = fragile
        self.__tva_reduc = reduc

    def description(self):
        """
            Retourne la description de la Piece
        """
        return self.__description

    def prix(self):
        """
            Retourne le prix de la Piece
        """
        return self.__prix

    def poids(self):
        """
            Retourne le poids de la Piece
        """
        return self.__poids

    def fragile(self):
        """
            Retourne True si fragile et False si non
        """
        return self.__is_fragile

    def tva_reduit(self):
        """
            Retourne True si en TVA réduit et false si non
        """
        return self.__reduc

    def __eq__(self,other):
        """
            Redéfinit l'égalité entre 2 objets Piece en fonction de leur description
        """
        return self.__description == other.__description and self.__prix == other.__prix

class ArticlePiece(Article):

    def __init__(self,n,piece):
        """ Créée un objet de type ArticlePiece en fonction du nombre n de Pieces piece

            Args:
                 n: int: le nombre de Piece
                 piece: obj: un objet Piece

            Returns:
                 Un objet de type ArticlePiece
        """
        self.__nombre = n
        self.__piece = piece

    def nombre(self):
        """
            Retourne le nombre de Piece
        """
        return self.__nombre

    def piece(self):
        """
            Retourne l'objet Piece piece
        """
        return self.__piece

    def description(self):
        """
            Retourne un string qui représente la Piece et son nombre
        """
        return str(self.__nombre) + " * " + self.__piece.description() + " @ " + str(self.__piece.prix())

    def prix(self):
        """
            Retourne le prix de tous les obj Piece
        """
        return self.__piece.prix() * self.__nombre

    def tva(self):
        """
            Retourne 21 si la TVA n'est pas réduite et 6 si non
        """
        if self.__piece.tva_reduit() == True:
            return 6
        return self.__piece.tva()


if __name__ == "__main__":
    d1 = ArticlePiece(3,Piece("Souris", 15, 0.150))
    d2 = ArticlePiece(2,Piece("clavier RGB", 150, 1.300))
    d3 = ArticlePiece(2,Piece("clavier", 30, 0.200))
    c = Facture("Yo", [d1,d2,d3])
    print(c.livraison_str())
