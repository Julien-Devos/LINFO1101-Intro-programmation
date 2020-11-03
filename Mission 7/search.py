def run_program():
    filename = input("Dans quel fichier souhaitez-vous travailler? ")

def print_lines(filename, l):
    pass

def readfile(filename):
    with open(filename, 'r') as file:
        return file.readlines()

def get_words(line):
    return line.strip().lower().split(' ')

def create_index(filename):
    pass

def get_lines(words,index):
    pass

if __name__ == "__main__":
    while True:
        run_program()