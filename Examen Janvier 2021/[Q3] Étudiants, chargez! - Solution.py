def load_students (filename) :      # NΕ PΑS EFFACER CΕTTE LIGNE
    """
    @pre:  filename est une chaîne de caractères
    @post: retourne un dictionnaire contenant pour chaque champ une liste des valeurs des étudiants, comme décrit dans l'énoncé de l'exercice.
    """
    lines = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                lines.append(line.strip())
    except:
        return {}

    try:
        students_nbr = int(lines[0])
    except:
        return {}

    champs = []
    for champ in lines[1].split(","):
        for caract in champ:
            if caract == ':':
                return {}
        champs.append(champ.strip())

    d = {champs[0]:[],champs[1]:[],champs[2]:[]}

    for i in range(2,students_nbr+2):
        student_inf = lines[i].split(',')

        for j in range(len(student_inf)):
            student_inf[j] = student_inf[j].split(":")

        for line in range(len(student_inf)):
            temp = []
            for inf in student_inf[line]:
                temp.append(inf.strip())
            student_inf[line] = temp

        pending_inf = [[champs[0],""],[champs[1],""],[champs[2],""]]
        count = 0
        for inf in student_inf:
            if len(student_inf) < 3 or 3 < len(student_inf):
                break
            elif inf[0].strip() == champs[0].strip():
                pending_inf[0][1] = inf[1]
                count += 1
            elif inf[0].strip() == champs[1].strip():
                pending_inf[1][1] = inf[1]
                count += 1
            elif inf[0].strip() == champs[2].strip():
                pending_inf[2][1] = inf[1]
                count += 1
        if count == 3:
            for inf in pending_inf:
                d[inf[0]].append(inf[1])
        else:
            break
    return d

#Note: 100%