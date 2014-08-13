tc = int ( input())
mod = 10**9+7
while tc != 0:
    num1,num2 = [int(x) for x in input().split()]
    print(num1**num2%mod)
    tc -= 1


