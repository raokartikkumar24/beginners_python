from math import log10

fibs = {}


def getdigits(i):
    if i > 0:
        return (int)(log10(i) + 1)
    else:
        return 1


fibarray = [50000]

fibarray[0] = 0
fibarray.append(1)
a = 0
b = 1
fibs[0]=1
for i in range(0, 100):
    c = a + b
    fibarray.append(c)
    dig = getdigits(c)
    fibs[c] = dig
    a = b
    b = c
#print(fibarray)
# print(fibs[3])
#print(fibs[4])
print(fibs)

