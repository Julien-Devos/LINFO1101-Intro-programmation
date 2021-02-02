def collect(file):
    collected = {}
    with open(file) as filename:
        for line in filename:
            pattern = treatment(extract(line.strip()))
            try:
                collected[pattern] += 1
            except KeyError:
                collected[pattern] = 1
    return collected