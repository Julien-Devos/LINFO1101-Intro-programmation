def translate(data, lan):
    words = data.lower().strip().split(" ")
    translated_data = ''
    for word in words:
        try:
            translated_data += lan[word] + " "
        except KeyError:
            translated_data += word + " "
    return translated_data.rstrip()