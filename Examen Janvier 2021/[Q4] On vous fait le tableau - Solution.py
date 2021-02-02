class Matrice :

    def __init__(self,m,n) :
        """
        pre: m ≥ 0, n ≥ 0
        post: Initialise une matrice de dimension m x n dont toutes les valeurs sont égales à 0.0
              La variable self.repr contient la représentation.
              Les variables self.m et self.n contiennent, respectivement, les dimensions
              m et n de la matrice.
        """
        self.m = m
        self.n = n
        self.repr = []

    def lignes(self) :
        """
        pre:  /
        post: retourne le nombre de lignes m de cette matrice
        """
        return self.m

    def colonnes(self) :
        """
        pre:  /
        post: retourne le nombre de colonnes n de cette matrice
        """
        return self.n

    def get(self,r,c) :
        """
        pre:  1 <= r <= m
              1 <= c <= n
        post: retourne la valeur de la cellule de la matrice à la ligne r et à la colonne c,
              ou 0.0 si aucune valeur n'a encore été attribuée à cette cellule
        """
        for i in self.repr:
            if i[0] == r and i[1] == c:
                return i[2]
        return 0.0

    def set(self,r,c,val) :
        """
        pre:  1 <= r <= m
              1 <= c <= n
        post: assigne la valeur val à la cellule de la matrice
              à la ligne r et à la colonne c
        """
        count = 0
        for i in range(len(self.repr)):
            if self.repr[i][0] == r and self.repr[i][1] == c:
                count += 1
                self.repr[i] = (self.repr[i][0],self.repr[i][1],val)
        if count == 0:
            self.repr.append((r, c, val))

    def __eq__(self,autre) :
        """
        pre:  /
        post: retourne True si autre est une instance de Matrice de mêmes dimensions et contenant
              les mêmes valeurs que cette matrice, False sinon
        """
        if isinstance(autre,Matrice) and self.m == autre.m and self.n == autre.n:
            for i in self.repr:
                count = 0
                for j in autre.repr:
                    if i == j or i[2] == 0.0 or j[2] == 0.0:
                        count += 1
                if count == 0:
                    return False
            #return True "correction ?"
        #return False "correction ?"
        return True #supprimer cette ligne

    def __str__(self):
        return self.repr

#Note 94%