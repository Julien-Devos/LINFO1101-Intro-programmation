def referee(score_file):
    with open(score_file, 'r') as file:
        l = []
        for i in file.readlines():
            l.append(i.strip().split(" "))
        team1, score1, team2, score2 = l[0][0], 0, l[1][0], 0
        l.remove(l[0])
        l.remove(l[0])
        for i in range(len(l)):
            if l[i][0] == team1:
                score1 += int(l[i][1])
            elif l[i][0] == team2:
                score2 += int(l[i][1])
        if score1 > score2:
            return team1
        else:
            return team2