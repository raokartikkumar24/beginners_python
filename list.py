__author__ = 'KRao4'
list1 = ["stark","lannister","baratheon","targareyn"]
print(list1[0])

suit_case = []
suit_case.append("the dark knight")
suit_case.append("inception")
suit_case.append("body of lies")
suit_case.append("inglorious basterds")

print(suit_case)

print(suit_case[0:2])
print(suit_case[2:3])

animals = "catdogfrog"

dog = animals[3:6]
cat = animals[:3] #from start until 3rd character
frog = animals[6:] #from 6th to end

print(dog,cat,frog)

ani = ["cat", "dog","cobra","penguin"]

cobra_index = ani.index("cobra")

print(cobra_index)

ani.insert(cobra_index,"lion")

print(ani)


#numbers in a list

numbers = [1,4,5,7,8,90]

for num in numbers:
    print(num**num)

numbers.sort()

print(numbers)


