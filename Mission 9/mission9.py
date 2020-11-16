"""
    Classes fournies pour la mission 9; Ã  complÃ©ter par les Ã©tudiants.
    @author Kim Mens
    @version 8 novembre 2020
"""

###############
### ARTICLE ###
###############

"""
    Cette classe reprÃ©sente un Article de facture simple,
    comprenant un descriptif et un prix.

    @author Kim Mens
    @version 18 novembre 2018
    (code adaptÃ© du code java de Charles Pecheur)
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
        Retourne le taux de TVA (mÃªme valeur pour chaque article)
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
    Cette classe reprÃ©sente une Facture, sous forme d'une liste d'articles.

    @author Kim Mens
    @version 18 novembre 2018
    (code adaptÃ© du code java de Charles Pecheur)
"""


class Facture:

    def __init__(self, description, articles):
        """
        CrÃ©e une facture avec une description (titre) et une liste d'articles.
        @pre  description est un string court dÃ©crivant la facture
              articles est une liste d'objets de type Article
        @post Une facture avec une description (titre) et un liste d'articles a Ã©tÃ© crÃ©e.
        """
        self.__reference = description
        self.__articles = articles

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
        Retourne la reprÃ©sentation string d'une facture, Ã  imprimer avec la mÃ©thode print().
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
        Imprime l'entÃªte de la facture, comprenant le descriptif et les tÃªtes de colonnes.
        """
        e = "Facture " + self.description() + "\n"
        e += self.barre_str()
        e += "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description", "prix HTVA", "TVA", "prix TVAC")
        e += self.barre_str()
        return e

    def barre_str(self):
        """
        Retourne un string reprÃ©sentant une barre horizontale sur la largeur de la facture.
        """
        b = ""
        barre_longeur = 83
        for i in range(barre_longeur):
            b += "="
        return b + "\n"

    def article_str(self, art):
        """
        Retourne un string correspondant Ã  une ligne de facture pour l'article art
        """
        return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(art.description(), art.prix(), art.tva(),
                                                                         art.prix_tvac())

    def totaux_str(self, prix, tva):
        """
        Retourne un string reprÃ©sentant une ligne de facture avec les totaux prix et tva, Ã  imprimer en bas de la facture
        """
        b = self.barre_str()
        b += "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format("T O T A L", prix, tva, prix + tva)
        b += self.barre_str()
        return b

    # Cette mÃ©thode doit Ãªtre ajoutÃ©e lors de l'Ã©tape 4 de la miasion
    def nombre(self, pce):
        """
        Retourne le nombre d'exemplaires de la piÃ¨ce pce dans la facture, en totalisant sur tous les articles qui concernent cette piÃ¨ce.
        """
        pass

    # Cette mÃ©thode doit Ãªtre ajoutÃ©e lors de l'Ã©tape 5 de la miasion
    def livraison_str(self):
        """
        Cette mÃ©thode est une mÃ©thode auxiliaire pour la mÃ©thode printLivraison
        """
        pass