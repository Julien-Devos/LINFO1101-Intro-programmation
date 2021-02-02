def extract(code):
    l = ""
    vowel = "aeiouy"
    consonant = "bcdefghjklmnpqrstvwxz"
    number = "0123456789"
    for i in code:
        if i in vowel:
            l = l + "vowel-low "

        elif i in vowel.upper():
            l = l + "vowel-up "

        elif i in number:
            l = l + "number "

        elif i in consonant:
            l = l + "consonant-low "

        else:
            l = l + "consonant-up "
    return l
