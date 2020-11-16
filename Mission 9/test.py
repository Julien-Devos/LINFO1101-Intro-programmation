"""
    Tests fournis pour la mission 9; Ã  complÃ©ter par les Ã©tudiants.
    @author Kim Mens
    @version 8 novembre 2020
"""

from mission9 import Article, Facture

"""
   Classe de test initiale pour la classe Article.
   @author Kim Mens
   @version 18 novembre 2018
"""


class TestArticleInitial:
    articles = [Article("laptop 15\" 8GB RAM", 743.79),
                Article("installation windows", 66.11),
                Article("installation wifi", 45.22),
                Article("carte graphique", 119.49)
                ]

    @classmethod
    def run(cls):
        for art in cls.articles:
            print(art)


"""
   Classe de test initiale pour la classe Facture.
   @author Kim Mens
   @version 8 novembre 2020
"""


class TestFactureInitial:
    facture = Facture("PC Store - 22 novembre", TestArticleInitial.articles)

    @classmethod
    def run(cls):
        print(cls.facture)


if __name__ == "__main__":
    print("*** TEST DE LA CLASSE Article ***")
    print()
    TestArticleInitial.run()

    print()
    print("*** TEST DE LA CLASSE Facture ***")
    print()
    TestFactureInitial.run()
