def create_dictionary(filename):
    with open(filename, 'r') as file:
        l = []
        for line in file.readlines():
            splited_line = line.strip().split()
            for line2 in splited_line:
                l.append(line2)
        d = {}
        for word in l:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
    return d

def occ(dictionary, word):
    try:
        return dictionary[word]
    except:
        return 0