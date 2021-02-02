def moyenne_mobile(lst,n) : # NE PAS EFFACER CETTE LIGNE
    """
    @pre: lst est une liste de réels non vide
    n un entier strictement positif : 0 <= n <= len(lst)//2
    @post: retourne une nouvelle liste contenant les moyennes mobiles
    calculées à partir de lst comme défini dans l'énoncé de cette question
    lst n'a pas été modifiée
    """
    final_list = []
    for i in range(len(lst)):
        row = 0
        test = []
        first = abs((i-n))
        if i < n:
            first = 0
        for j in lst[first:i]:
            test.append(j)
            row += j
        for k in lst[i:i+n+1]:
            test.append(k)
            row += k
        final_list.append(row/len(test))
    return final_list

#Note: 100%