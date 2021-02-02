def rho(a, b, c):
    return b ** 2 - 4 * a * c


def n_solutions(a, b, c):
    delta = rho(a, b, c)

    if delta == 0:
        return 1

    elif delta > 0:
        return 2

    else:
        return 0


def solution(a, b, c):
    delta = rho(a, b, c)
    solutions = n_solutions(a, b, c)
    root = racine_carree(delta)

    if solutions == 1:
        return -b / (2 * a)

    elif solutions == 2:
        if ((-b - root) / (2 * a) > (-b + root) / (2 * a)):
            return (-b + root) / (2 * a)
        else:
            return (-b - root) / (2 * a)

