# Résolution d'une equation diophantienne de type x**a + y**b = z**c
# Devos Bryan et Devos Julien Septembre 2020

a = int(input("Entrez la valeur de la puissance a: "))   #Permet de rentrer les valeurs de a, b, c
b = int(input("Entrez la valeur de la puissance b: "))
c = int(input("Entrez la valeur de la puissance c: "))
solutions = 0
                                              #Nous avons choisi de faire boucler jusqu'à 100 pour éviter les temps excessifs
for x in range(1, 100):                       #La boucle va vérifier les différentes solutions possibles pour x=une valeur
    for y in range(1, 100):                   #La boucle va vérifier les différentes solutions possibles pour y=une valeur
        for z in range(1, 100):               #La boucle va vérifier les différentes solutions possibles pour z=une valeur
            if x**a + y**b == z**c:        #On vérifie si l'équation est correcte
                common_div = 0
                for div in range(2, 100):  #Ce passage sert a définir si les racines possèdent un ou plusiers diviseurs communs
                    if (x%div == 0 and y%div == 0) or (x%div == 0 and z%div == 0) or (y%div == 0 and z%div == 0):
                        common_div +=1
                if common_div == 0:
                    solutions += 1
                    print(str(solutions) + ") x =", x, " y =", y, " z =", z)

if solutions == 0:
    print("Il n'y a aucune solution où les racines ne possèdent aucun diviseur commun pour l'équation: x**"+str(a)+" + y**"+str(b)+" = z**"+str(c))

else:
    if solutions == 1:
        print("Il y a", solutions, "solution qui a été trouvé.")
    else:
        print("Il y a",solutions,"solutions qui ont été trouvées.")
