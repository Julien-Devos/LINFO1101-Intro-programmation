def fine(authorized_speed, actual_speed):
    over_speed = actual_speed - authorized_speed
    if over_speed <= 0:
        return 0

    elif over_speed > 10:
        return 5 * over_speed * 2

    elif 5 * over_speed < 12.5:
        return 12.5

    else:
        return 5 * over_speed