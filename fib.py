from math import log10


def getdigits(i):
    if i > 0:
        return (int)(log10(i) + 1)
    else:
        return 1

fibs = {}
def generate():
	a = 0
	b = 1
	fibs[0]=1
	for i in range(1, 5000):
		c = a + b
		dig = getdigits(c)
		if dig not in fibs:
			fibs[dig] = i+1
		a = b
		b = c
		
		



if __name__ == "__main__":
	t = (int)(input())
	generate()
	while t != 0:
		N = (int)(input())
		print( fibs[N] )
		t -= 1




#print(fibs)

