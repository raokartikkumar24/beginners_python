dic = {}
marks = []
li = []
N = (int)(input())
C = 0
while N != 0:
	li = [x for x in input().split()]
	marks = li[1:len(li)]
	dic[li[0]] = marks
	C += 1
	N -= 1
# print(dic)
naam = input()
# print(dic[naam])
# print(dic[li[0]])
sum = 0
for i in range(0,len(marks)):
	sum += float(dic[naam][i])
print("%.2f" % float(sum/len(marks)))

# print(dic)
# print(li)
