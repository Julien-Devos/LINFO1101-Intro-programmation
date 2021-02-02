def translate(data):
    try:
        morse_data = ''
        for car in data:
            morse_data += morse[car]
        return morse_data
    except:
        raise TypeError