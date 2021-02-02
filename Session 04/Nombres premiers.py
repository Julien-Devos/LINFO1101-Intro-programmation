def primes(max):
    list = []
    if max > 0:
        for i in range(2, max+1):
            prime = True
            for j in range(2, i):
                if i%j == 0:
                    prime = False
            if prime:
                list.append(i)
    return list