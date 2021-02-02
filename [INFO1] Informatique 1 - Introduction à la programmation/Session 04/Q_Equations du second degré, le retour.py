def solveur(l):
    solv = []
    for i in range(len(l)):
        solv.append(solution(l[i][0],l[i][1],l[i][2]))
    return solv