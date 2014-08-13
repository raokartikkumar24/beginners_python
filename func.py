__author__ = 'KRao4'
def cube(number):
    number = number*number*number
    print(number)
def max_sum(*args):
    print(max(args))
def min_sum(*args):
    print(min(args))
cube(3)
max_sum(10,20,-90,100)
min_sum(10,33,-999,-19)
print(type(42))
if type(42) == int:
    print("integer")
elif type(42.23) == float:
    print("float!!")
else:
    print("nothing")
