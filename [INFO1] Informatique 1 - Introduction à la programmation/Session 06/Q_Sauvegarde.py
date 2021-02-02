def save_data(filename, life, mana, position_x, position_y):
    with open(filename, 'w') as file:
        l = [str(life) + "\n", str(mana) + "\n", str(position_x) + "\n", str(position_y) + "\n"]
        file.writelines(l)


def load_data(filename):
    try:
        with open(filename, 'r') as file:
            l = []
            for i in file.readlines():
                l.append(int(i.strip()))
        return tuple(l)
    except:
        raise FileNotFoundError