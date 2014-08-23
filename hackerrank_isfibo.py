from math import sqrt
t = (int)(input())

while t != 0:
    N = (int)(input())
    d1 = 5*(N**2) + 4
    d2 = 5*(N**2) - 4
    
    if sqrt(d1)%1 ==0 or sqrt(d2)%1==0:
        print("IsFibo")
    else:
        print("IsNotFibo")
    t -= 1