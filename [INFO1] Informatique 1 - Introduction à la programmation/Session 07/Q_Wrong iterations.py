sum_even = 0
i = 0
while i < len(matrix):
    mat = iter(matrix[i])
    while True:
        try:
            value = next(mat)
            if value%2 == 0:
                sum_even += value
        except StopIteration:
            break
    i += 1