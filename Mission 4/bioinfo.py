import collections

def is_correct(PRNG):
    """
    pre: Un générateur de nombre aléatoire
    post: si le PRNG est aléatoire retourne True, False si non
    """
    list_of_randoms_sequences = []
    interval_max = 10
    #create list of number sequence for each seed
    for i in range(100):
        prng = PRNG(i, interval_max)
        list_of_randoms_sequences.append([prng.next_int() for _ in range(50)])
    if is_same_sequence_seed(PRNG, list_of_randoms_sequences) and one_sequence_exists(list_of_randoms_sequences) and number_in_interval(interval_max, list_of_randoms_sequences) and frequence_number(list_of_randoms_sequences, interval_max):
        return True
    return False

def is_same_sequence_seed(PRNG, list_of_randoms_sequences):
    """
    pre: Un PRNG, une liste de liste de suite de nombre aléatoire généré pour chaque seed de 0 à length de list_of_randoms
    post: retourn True si le générateur génère bien la même suite pour chaque nombre, False dans le cas inverse
    """
    for i, sequence in enumerate(list_of_randoms_sequences):
        prng = PRNG(i, 10)
        if [prng.next_int() for _ in range(50)] != sequence:
            return False
    return True

def one_sequence_exists(list_of_randoms_sequences):
    """
    pre: une liste de liste de suite de nombre aléatoire généré pour chaque seed de 0 à length de list_of_randoms
    post: retourne True si pour chaque séquence il n'en existe qu'une dans la liste, False si il en y a plus d'une
    """
    for sequence in list_of_randoms_sequences:
        if list_of_randoms_sequences.count(sequence) > 1:
            return False
    return True

def number_in_interval(interval_max, list_of_randoms_sequences):
    """
    pre:
        interval_max -> nombre entier > 0 représentant l'interval max sur lequel les nombre àléatoire sont
        list_of_randoms_sequences -> une liste de liste de suite de nombre aléatoire généré pour chaque seed de 0 à length de list_of_randoms
    post: retourne True si touts les nombres aléatoire respecte l'interval donné et sont tous présent
    """
    for sequence in list_of_randoms_sequences:
        #if interval_max != len(list(set(sequence))): return False
        for n in sequence:
            if n not in list(range(interval_max)): return False
    return True

def frequence_number(list_of_randoms_sequences, max_interval):
    """
    pre: list_of_randoms_sequences -> une liste de liste de suite de nombre aléatoire généré pour chaque seed de 0 à length de list_of_randoms
       max_interval -> nombre entier positif représentant le chiffre maximum possible dans les listes
    post: vérifie la fréquence de chaque nombre dans une liste, si un nombre trop fréquent ou pas assez retourne False, True inversément
    """
    presence_min = 1
    presence_max = 15
    for sequence in list_of_randoms_sequences:
        counter = collections.Counter(sequence)
        for n in range(1, max_interval):
            if n in counter:
                if counter[n] < presence_min or counter[n] > presence_max: return False
    return Trueimport collections

def is_correct(PRNG):
    """
    pre: Un générateur de nombre aléatoire
    post: si le PRNG est aléatoire retourne True, False si non
    """
    list_of_randoms_sequences = []
    interval_max = 10
    #create list of number sequence for each seed
    for i in range(100):
        prng = PRNG(i, interval_max)
        list_of_randoms_sequences.append([prng.next_int() for _ in range(50)])
    if is_same_sequence_seed(PRNG, list_of_randoms_sequences) and one_sequence_exists(list_of_randoms_sequences) and number_in_interval(interval_max, list_of_randoms_sequences) and frequence_number(list_of_randoms_sequences, interval_max):
        return True
    return False

def is_same_sequence_seed(PRNG, list_of_randoms_sequences):
    """
    pre: Un PRNG, une liste de liste de suite de nombre aléatoire généré pour chaque seed de 0 à length de list_of_randoms
    post: retourn True si le générateur génère bien la même suite pour chaque nombre, False dans le cas inverse
    """
    for i, sequence in enumerate(list_of_randoms_sequences):
        prng = PRNG(i, 10)
        if [prng.next_int() for _ in range(50)] != sequence:
            return False
    return True

def one_sequence_exists(list_of_randoms_sequences):
    """
    pre: une liste de liste de suite de nombre aléatoire généré pour chaque seed de 0 à length de list_of_randoms
    post: retourne True si pour chaque séquence il n'en existe qu'une dans la liste, False si il en y a plus d'une
    """
    for sequence in list_of_randoms_sequences:
        if list_of_randoms_sequences.count(sequence) > 1:
            return False
    return True

def number_in_interval(interval_max, list_of_randoms_sequences):
    """
    pre:
        interval_max -> nombre entier > 0 représentant l'interval max sur lequel les nombre àléatoire sont
        list_of_randoms_sequences -> une liste de liste de suite de nombre aléatoire généré pour chaque seed de 0 à length de list_of_randoms
    post: retourne True si touts les nombres aléatoire respecte l'interval donné et sont tous présent
    """
    for sequence in list_of_randoms_sequences:
        #if interval_max != len(list(set(sequence))): return False
        for n in sequence:
            if n not in list(range(interval_max)): return False
    return True

def frequence_number(list_of_randoms_sequences, max_interval):
    """
    pre: list_of_randoms_sequences -> une liste de liste de suite de nombre aléatoire généré pour chaque seed de 0 à length de list_of_randoms
       max_interval -> nombre entier positif représentant le chiffre maximum possible dans les listes
    post: vérifie la fréquence de chaque nombre dans une liste, si un nombre trop fréquent ou pas assez retourne False, True inversément
    """
    presence_min = 1
    presence_max = 15
    for sequence in list_of_randoms_sequences:
        counter = collections.Counter(sequence)
        for n in range(1, max_interval):
            if n in counter:
                if counter[n] < presence_min or counter[n] > presence_max: return False
    return Trueimport collections

def is_correct(PRNG):
    """
    pre: Un générateur de nombre aléatoire
    post: si le PRNG est aléatoire retourne True, False si non
    """
    list_of_randoms_sequences = []
    interval_max = 10
    #create list of number sequence for each seed
    for i in range(100):
        prng = PRNG(i, interval_max)
        list_of_randoms_sequences.append([prng.next_int() for _ in range(50)])
    if is_same_sequence_seed(PRNG, list_of_randoms_sequences) and one_sequence_exists(list_of_randoms_sequences) and number_in_interval(interval_max, list_of_randoms_sequences) and frequence_number(list_of_randoms_sequences, interval_max):
        return True
    return False

def is_same_sequence_seed(PRNG, list_of_randoms_sequences):
    """
    pre: Un PRNG, une liste de liste de suite de nombre aléatoire généré pour chaque seed de 0 à length de list_of_randoms
    post: retourn True si le générateur génère bien la même suite pour chaque nombre, False dans le cas inverse
    """
    for i, sequence in enumerate(list_of_randoms_sequences):
        prng = PRNG(i, 10)
        if [prng.next_int() for _ in range(50)] != sequence:
            return False
    return True

def one_sequence_exists(list_of_randoms_sequences):
    """
    pre: une liste de liste de suite de nombre aléatoire généré pour chaque seed de 0 à length de list_of_randoms
    post: retourne True si pour chaque séquence il n'en existe qu'une dans la liste, False si il en y a plus d'une
    """
    for sequence in list_of_randoms_sequences:
        if list_of_randoms_sequences.count(sequence) > 1:
            return False
    return True

def number_in_interval(interval_max, list_of_randoms_sequences):
    """
    pre:
        interval_max -> nombre entier > 0 représentant l'interval max sur lequel les nombre àléatoire sont
        list_of_randoms_sequences -> une liste de liste de suite de nombre aléatoire généré pour chaque seed de 0 à length de list_of_randoms
    post: retourne True si touts les nombres aléatoire respecte l'interval donné et sont tous présent
    """
    for sequence in list_of_randoms_sequences:
        #if interval_max != len(list(set(sequence))): return False
        for n in sequence:
            if n not in list(range(interval_max)): return False
    return True

def frequence_number(list_of_randoms_sequences, max_interval):
    """
    pre: list_of_randoms_sequences -> une liste de liste de suite de nombre aléatoire généré pour chaque seed de 0 à length de list_of_randoms
       max_interval -> nombre entier positif représentant le chiffre maximum possible dans les listes
    post: vérifie la fréquence de chaque nombre dans une liste, si un nombre trop fréquent ou pas assez retourne False, True inversément
    """
    presence_min = 1
    presence_max = 15
    for sequence in list_of_randoms_sequences:
        counter = collections.Counter(sequence)
        for n in range(1, max_interval):
            if n in counter:
                if counter[n] < presence_min or counter[n] > presence_max: return False
    return Trueimport collections

def is_correct(PRNG):
    """
    pre: Un générateur de nombre aléatoire
    post: si le PRNG est aléatoire retourne True, False si non
    """
    list_of_randoms_sequences = []
    interval_max = 10
    #create list of number sequence for each seed
    for i in range(100):
        prng = PRNG(i, interval_max)
        list_of_randoms_sequences.append([prng.next_int() for _ in range(50)])
    if is_same_sequence_seed(PRNG, list_of_randoms_sequences) and one_sequence_exists(list_of_randoms_sequences) and number_in_interval(interval_max, list_of_randoms_sequences) and frequence_number(list_of_randoms_sequences, interval_max):
        return True
    return False

def is_same_sequence_seed(PRNG, list_of_randoms_sequences):
    """
    pre: Un PRNG, une liste de liste de suite de nombre aléatoire généré pour chaque seed de 0 à length de list_of_randoms
    post: retourn True si le générateur génère bien la même suite pour chaque nombre, False dans le cas inverse
    """
    for i, sequence in enumerate(list_of_randoms_sequences):
        prng = PRNG(i, 10)
        if [prng.next_int() for _ in range(50)] != sequence:
            return False
    return True

def one_sequence_exists(list_of_randoms_sequences):
    """
    pre: une liste de liste de suite de nombre aléatoire généré pour chaque seed de 0 à length de list_of_randoms
    post: retourne True si pour chaque séquence il n'en existe qu'une dans la liste, False si il en y a plus d'une
    """
    for sequence in list_of_randoms_sequences:
        if list_of_randoms_sequences.count(sequence) > 1:
            return False
    return True

def number_in_interval(interval_max, list_of_randoms_sequences):
    """
    pre:
        interval_max -> nombre entier > 0 représentant l'interval max sur lequel les nombre àléatoire sont
        list_of_randoms_sequences -> une liste de liste de suite de nombre aléatoire généré pour chaque seed de 0 à length de list_of_randoms
    post: retourne True si touts les nombres aléatoire respecte l'interval donné et sont tous présent
    """
    for sequence in list_of_randoms_sequences:
        #if interval_max != len(list(set(sequence))): return False
        for n in sequence:
            if n not in list(range(interval_max)): return False
    return True

def frequence_number(list_of_randoms_sequences, max_interval):
    """
    pre: list_of_randoms_sequences -> une liste de liste de suite de nombre aléatoire généré pour chaque seed de 0 à length de list_of_randoms
       max_interval -> nombre entier positif représentant le chiffre maximum possible dans les listes
    post: vérifie la fréquence de chaque nombre dans une liste, si un nombre trop fréquent ou pas assez retourne False, True inversément
    """
    presence_min = 1
    presence_max = 15
    for sequence in list_of_randoms_sequences:
        counter = collections.Counter(sequence)
        for n in range(1, max_interval):
            if n in counter:
                if counter[n] < presence_min or counter[n] > presence_max: return False
    return Trueimport collections

def is_correct(PRNG):
    """
    pre: Un générateur de nombre aléatoire
    post: si le PRNG est aléatoire retourne True, False si non
    """
    list_of_randoms_sequences = []
    interval_max = 10
    #create list of number sequence for each seed
    for i in range(100):
        prng = PRNG(i, interval_max)
        list_of_randoms_sequences.append([prng.next_int() for _ in range(50)])
    if is_same_sequence_seed(PRNG, list_of_randoms_sequences) and one_sequence_exists(list_of_randoms_sequences) and number_in_interval(interval_max, list_of_randoms_sequences) and frequence_number(list_of_randoms_sequences, interval_max):
        return True
    return False

def is_same_sequence_seed(PRNG, list_of_randoms_sequences):
    """
    pre: Un PRNG, une liste de liste de suite de nombre aléatoire généré pour chaque seed de 0 à length de list_of_randoms
    post: retourn True si le générateur génère bien la même suite pour chaque nombre, False dans le cas inverse
    """
    for i, sequence in enumerate(list_of_randoms_sequences):
        prng = PRNG(i, 10)
        if [prng.next_int() for _ in range(50)] != sequence:
            return False
    return True

def one_sequence_exists(list_of_randoms_sequences):
    """
    pre: une liste de liste de suite de nombre aléatoire généré pour chaque seed de 0 à length de list_of_randoms
    post: retourne True si pour chaque séquence il n'en existe qu'une dans la liste, False si il en y a plus d'une
    """
    for sequence in list_of_randoms_sequences:
        if list_of_randoms_sequences.count(sequence) > 1:
            return False
    return True

def number_in_interval(interval_max, list_of_randoms_sequences):
    """
    pre:
        interval_max -> nombre entier > 0 représentant l'interval max sur lequel les nombre àléatoire sont
        list_of_randoms_sequences -> une liste de liste de suite de nombre aléatoire généré pour chaque seed de 0 à length de list_of_randoms
    post: retourne True si touts les nombres aléatoire respecte l'interval donné et sont tous présent
    """
    for sequence in list_of_randoms_sequences:
        #if interval_max != len(list(set(sequence))): return False
        for n in sequence:
            if n not in list(range(interval_max)): return False
    return True

def frequence_number(list_of_randoms_sequences, max_interval):
    """
    pre: list_of_randoms_sequences -> une liste de liste de suite de nombre aléatoire généré pour chaque seed de 0 à length de list_of_randoms
       max_interval -> nombre entier positif représentant le chiffre maximum possible dans les listes
    post: vérifie la fréquence de chaque nombre dans une liste, si un nombre trop fréquent ou pas assez retourne False, True inversément
    """
    presence_min = 1
    presence_max = 15
    for sequence in list_of_randoms_sequences:
        counter = collections.Counter(sequence)
        for n in range(1, max_interval):
            if n in counter:
                if counter[n] < presence_min or counter[n] > presence_max: return False
    return True