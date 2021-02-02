with open(filename, 'r') as file:
    data = []
    for i in file.readlines():
        data.append(i.strip())
m = int(data[0])
n = int(data[1])
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(0.0)
    matrix.append(row)
for i in range(2,len(data)):
    curr = data[i].split(" ")
    curr[0] = curr[0].split(",")
    matrix[int(curr[0][0])][int(curr[0][1])] = float(curr[1])
return matrix