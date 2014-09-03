from math import sqrt
t= (int)(input())
while t != 0:
	A,B = [int(x) for x in input().split()]
	count = 0
	for i in range(A,B+1):
		if (sqrt(i)%1) == 0:
			count+=1
	print(count)
	t -= 1
		
		
	