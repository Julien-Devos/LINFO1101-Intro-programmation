def get_country(l, name):
    for i in l:
        if i["City"] == name:
            return i["Country"]
    return False