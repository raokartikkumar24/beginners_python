__author__ = 'KRao4'
array =[]

def getmincount(n):

    print(len(array))
    i = 2
    while i != n+1:
        #array.append(1+array.index(i-1))
        array[i] = 1 + array[i-1];
        if(i%2==0):
            array.append(min( array[i] , 1+ array[i//2] ))
        if(i%3==0):
             array.append(min( array[i] , 1+ array[i//33] ))
        i += 1

    return array[n]

n = int(input())
count = 0;
while count != 2:
    array.append(0)
    count+=1

print(getmincount(n))
