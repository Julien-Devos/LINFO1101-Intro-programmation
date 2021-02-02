#Devos Julien
a=1
b=1
c=1
d=1

while a<=10:
    print(a, "\t", b, "\t", c, "\t", d)
    a += 1
    b = a*a
    c += b
    d = a*(a+1)*(2*a+1)//6