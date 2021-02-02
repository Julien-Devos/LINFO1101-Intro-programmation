"""
    Tests fournis pour la mission 9; à  complèter par les étudiants.
    @author Kim Mens
    @version 8 novembre 2020
"""

from mission9 import Article, Facture, Piece, ArticleReparation, ArticlePiece

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
    a1 = ArticlePiece(2, Piece("Micro-onde RGB RAZER 15W", 599.99, 1.575))
    a2 = ArticlePiece(7, Piece("Assiette Logitech Chauffante", 39.89, 1.387, True))
    a3 = ArticlePiece(1, Piece("Set 1x Fourchette, 1x Couteau Apple", 121.00, 0.057))
    a4 = ArticlePiece(250, Piece("PROMO Serviette", 0.59, 0.02, False, True))
    a5 = ArticlePiece(4, Piece("Verre Noctua", 12.89, 0.186, True))
    a6 = ArticlePiece(4, Piece("Sous-Verre Razer RGB", 87.90, 0.103, True))
    a7 = ArticlePiece(3, Piece("XBOX series X Frigo", 1250, 124.300))
    a8 = ArticlePiece(1, Piece("Iphone 12 Pro MAX",1259,0.226,True))

    facture = Facture("PC Store - 22 novembre", TestArticleInitial.articles)
    articlesRep = [ArticleReparation(10),
                  ArticleReparation(2),
                  ArticleReparation(0),
                  ArticleReparation(42)
                  ]
    articlesPiece = [a1,a2,a3,a4,a5,a6,a7,a8]
    livraisons = [Facture("Fan d'apple",[a3,a8]),
                  Facture("Livraison frigo",[a7]),
                  Facture("J'aime les serpents qui brillent",[a1,a6]),
                  Facture("J'aime Bill Gates",[a7]),
                  Facture("J'achète tout le shop",[a1,a2,a3,a4,a5,a6,a7,a8])]


    @classmethod
    def run(cls):
        print(cls.facture)

        print("\n*** TEST DE ArticlesReparation ***\n")

        #test for ArticleReparation
        for rep in cls.articlesRep:
            print(rep)

        print("\n*** TEST DE ArticlesPiece ***\n")

        for piece in cls.articlesPiece:
            print(piece.description())
            print(piece)

        print("\n*** TEST DE livraison_str() ***\n")

        for livraison in cls.livraisons:
            print(livraison.livraison_str())


if __name__ == "__main__":
    print("*** TEST DE LA CLASSE Article ***")
    print()
    TestArticleInitial.run()

    print()
    print("*** TEST DE LA CLASSE Facture ***")
    print()
    TestFactureInitial.run()