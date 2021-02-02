greatest_divisor = None
for i in range(1, a):
    if a%i == 0:
        greatest_divisor = i
return greatest_divisor