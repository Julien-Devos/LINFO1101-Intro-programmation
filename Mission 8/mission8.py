class Duree:
    def __init__(self,h,m,s):
        """ Initialise un objet Duree ayant pour attributs hour, minute et sec
            Si m ou s vaut plus que 60, on corrige les valeurs avec sec_correct

            Args:
                h: int: un nombre d'heure
                m: int: un nombre de minutes
                s: int: un nombre de secondes
        """
        self.hour = h
        self.minute = m
        self.sec = s
        if m >= 60 and s >= 60:
            self.sec_correct()

    def sec_correct(self):
        """
        Modifie hour minute et sec de l'objet self pour que minute et sec ne dépassent pas 60
        """
        tot_sec = self.to_secondes()
        self.hour = tot_sec // 3600
        self.minute = (tot_sec % 3600) // 60
        self.sec = (tot_sec % 3600) % 60

    def to_secondes(self):
        """
        Retourne le nombre total de secondes de cette instance de Duree (self).
        """
        seconds = (self.hour*3600)+(self.minute*60)+(self.sec)
        return seconds

    def delta(self, d):
        """
        Retourne la différence entre cette instance de Duree (self) et la Duree d passée en paramètre,
        en secondes (positif si ce temps-ci est plus grand).
        """
        diff = d.to_secondes() - self.to_secondes()
        return diff

    def apres(self, d):
        """
        Retourne True si cette instance de Duree (self) est plus grand que la Duree d passée en paramètre;
        retourne False sinon.
        """
        if self.delta(d) < 0:
            return True
        else:
            return False

    def ajouter(self, d):
        """
        Ajoute une autre Duree d à cette instance de Duree (self).
        Corrige de manière à ce que les minutes et les secondes soient dans l'intervalle [0..60[,
        en reportant au besoin les valeurs hors limites sur les unités supérieures.
        """
        self.hour += d.hour
        self.minute += d.minute
        self.sec += d.sec
        self.sec_correct()

    def __str__(self):
        """
        Retourne cette durée sous la forme de texte "heures:minutes:secondes".
        Astuce: la méthode "{:02}:{:02}:{:02}".format(heures, minutes, secondes)
        retourne le String désiré avec les nombres en deux chiffres en ajoutant
        les zéros nécessaires.
        """
        return ("{:02}:{:02}:{:02}".format(self.hour, self.minute, self.sec))

class Chanson :
    def __init__(self,t,a,d):
        """ Initialise un objet Chanson ayant pour attributs titre, auteur et duree

            Args:
                t: str: le titre de la chanson
                a: str: le nom de l'auteur de la chanson
                d: obj: un objet Duree
        """
        self.titre = t
        self.auteur = a
        self.duree = d.__str__()

    def __str__(self):
        """
        Retourne un String décrivant cette chanson sous le format "TITRE - AUTEUR - DUREE".
        Par exemple: "Let's_Dance - David_Bowie - 00:04:05"
        """
        return ("{} - {} - {}".format(self.titre,self.auteur,self.duree))

class Album :
    def __init__(self,n):
        """ Initialise un objet Album ayant pour attributs name, total_duree et dic

            Args:
                n: str: le nom de l'album
        """
        self.name = n
        self.total_duree = Duree(0,0,0)
        self.dic = {"total_time":0,"total_song":0}

    def ajouter(self,song):
        """ Ajoute une musique à self.dic le dictionaire de l'album

            Args:
                song: obj: un objet Chanson
        """
        duree = song.duree.split(":")
        self.total_duree.ajouter(Duree(int(duree[0]), int(duree[1]), int(duree[2])))
        if (self.total_duree.to_secondes() / 60) <= 75:
            for i in range(1,101):
                if i not in self.dic:
                    self.dic["total_song"] += 1
                    self.dic[i] = {"song": song}
                    self.dic["total_time"] = self.total_duree.__str__()
                    return None
        return False

    def __str__(self):
        """
        Retourne un String décrivant l'album.
        """
        album_text = "Album " + self.name + " (" + str(self.dic["total_song"]) + " chansons, " + self.dic["total_time"] + ")\n"
        for i in self.dic:
            if i != "total_time" and i != "total_song":
                album_text += str(i) + ": " + self.dic[i]["song"].__str__() + "\n"
        return album_text

if __name__ == "__main__":
    # Grace à  la ligne ci-dessus, le code ci-dessous ne sera exécuter que si on n'exécute ce fichier directement.
    # Ceci nous permet d'éviter que le code ci-dessous sera exécuté lorsqu'on fait un import de ce fichier,
    # par exemple dans notre fichier test.py

    with open("music-db.txt", 'r') as file:
        song_list = []
        for line in file:
            song_list.append(line.strip())

        album = Album(str(1))
        count = 1
        for song_number in range(len(song_list)):
            song = song_list[song_number].split(" ")
            value = album.ajouter(Chanson(song[0],song[1],Duree(0,int(song[2]),int(song[3]))))
            if value == False:
                count += 1
                print(album)
                album = Album(str(count))
                value = album.ajouter(Chanson(song[0], song[1], Duree(0, int(song[2]), int(song[3]))))
        print(album)

        temps1 = Duree(15, 10, 52)
        temps2 = Duree(0, 15, 32)
        temps3 = Duree(3, 7, 1)
        temps4 = Duree(127, 64, 87)
        temps4.ajouter(temps1)
        print(temps4)