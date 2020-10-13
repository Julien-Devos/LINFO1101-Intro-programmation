def is_adn(s):
    if s == "":
        return False

    for i in s:
        if i == "a" or i == "A" or i == "t" or i == "T" or i == "c" or i == "C" or i == "g" or i == "G":
            pass
        else:
            return False

    return True

print(is_adn("aAaza"))
