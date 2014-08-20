def fact(n):
	if n == 0:
		return 1
	else:
		return n*fact(n-1)


if __name__ == "__main__":
	N = (int)(input())
	
	listsum = 0
	for j in range(10,N):
		list = {}
		list = str(j)
		sum = 0
		for i in range(0,len(list)):
			sum+= fact(int(list[i]))
	
	
		if sum%j == 0:
			listsum+=j
	
	print(listsum)


