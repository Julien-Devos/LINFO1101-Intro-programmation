s=""
def is_adn(s):
    for e in s:
        if e=="a" or e=="A" or e=="t" or e=="T" or e=="c" or e=="C" or e=="g" or e=="G":
            pass
        else:
            return False
    return True
print(is_adn(s))

def positions(s, p):
    for e in s:
        if e == p[0]:
