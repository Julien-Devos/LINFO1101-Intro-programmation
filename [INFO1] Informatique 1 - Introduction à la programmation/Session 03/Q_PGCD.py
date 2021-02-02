def gcd(a,b):
    greatest = None
    for k in range(1, b+1):
        if a%k == 0 and b%k == 0:
            greatest = k
    return greatest