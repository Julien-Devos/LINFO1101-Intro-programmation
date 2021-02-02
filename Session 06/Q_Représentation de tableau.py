def table(filename_in, filename_out, width):
    with open(filename_in, 'r') as file_in:
        names = file_in.readlines()
    with open(filename_out, 'w') as file_out:
        s = "+-" + width*"-" + "-+\n"
        for name in names:
            s += "| {0:{1}} |\n".format(name[0:width].strip(),width)
        s += "+-" + width*"-" + "-+"
        file_out.write(s)