def write(letter_template, name):
    with open(letter_template, 'r') as file:
        s = file.read().replace("#",name)
    with open(letter_template, 'w') as file:
        file.write(s)