s="acga"
def is_adn(s):
    for e in s:
        if e=="a" or e=="A" or e=="t" or e=="T" or e=="c" or e=="C" or e=="g" or e=="G":
            return True
        else:
            return False
print(is_adn(s))