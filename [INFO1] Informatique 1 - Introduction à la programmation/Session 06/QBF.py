def get_max(filename):
    max = -1
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    if float(line.strip()) > max:
                        max = float(line.strip())
                except:
                    pass
    except:
        pass
    return max