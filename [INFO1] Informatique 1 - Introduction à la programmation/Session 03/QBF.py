def chiffres_pairs(n):
    """ Retourne True si le nombre de chiffres de n est pair et False si non

        Args:
            n: int: un entier

        Returns:
            True si le nombre de chiffres de n est pair et False si non
    """
    count = 1
    while n >= 10:
        n //= 10
        count += 1
    if count % 2 == 0:
        return True
    return False