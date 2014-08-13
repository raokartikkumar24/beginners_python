__author__ = 'KRao4'
bool_one = (20-10 ) > 15

bool_two = (10+17)==3**16

bool_three = 1**2 <= -1

bool_four =  40*4 >= -4

bool_five = 100 != 10**2

print( bool_one, bool_two, bool_three, bool_four, bool_five)

bool_1 = True and False
bool_2 = False and False
bool_3 = 3*3 < 10.5 and False

bool_11 = True or False
bool_123 = 11 or 3 < 4

bool_not = not True
bool_n = not not 4 < 5

print(bool_n, bool_11, bool_not, bool_1 ,bool_2, bool_3)


bool_po = False or  not True and False or False and not True
print( bool_po)

bool_qw = False and not True or False
print(bool_qw)


def using_control_once():
    if 10 == 5*2:
        return "Success #1"

def using_control_again():
    if 5 == 25/5:
        return "Success #2"

print( using_control_once())
print (using_control_again())


def greater_less_equal_5(answer):
    if answer > 5 :
        return 1
    elif answer < 5:
        return -1
    else:
        return 0

print (greater_less_equal_5(4))
print (greater_less_equal_5(5))
print (greater_less_equal_5(6))
