def quetelet(height, weight):
    bimi = weight/(height**2)
    if bimi < 20:
        return "thin"
    elif 20 <= bimi <= 25:
        return "normal"
    elif 25 < bimi <= 30 :
        return "overweight"
    else:
        return "obese"