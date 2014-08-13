__author__ = 'KRao4'
array = []
def getmin(n):
    if n==1:
        return 0
    if array[n] != -1:
        #print(n)
        return array[n]
    r = 1 + getmin(n-1)
    if r%2 ==0:
        r = min(r,1+getmin(n//2))
    if r%3 ==0:
        r = min(r,1+getmin(n//3))
    array[n] = r
    return r+1



n = int( input())
count = 0
while count != n+1:
    array.append(-1)
    count +=1

print(getmin(n))






