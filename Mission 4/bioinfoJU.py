def is_adn(s):
    adn = False
    if s == "":
        return False

    for i in s:
        if i == "a" or i == "A" or i == "t" or i == "T" or i == "c" or i == "C" or i == "g" or i == "G":
            adn = True
        else:
            return False

    return adn

print(is_adn("aAaza"))
