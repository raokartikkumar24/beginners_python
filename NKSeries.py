__author__ = 'KRao4'

modvale = 10**9+7

t = (int)(input())

while t != 0:
    n,k = [int(x) for x in input().split()]
    sum = 0

    for i in range(1,n+1):
        sum+=i**k
    print(sum%modvale)
    t-=1
