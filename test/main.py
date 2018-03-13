# x = 3
# y = 3.0
# print (x is y)
# print (x == y)

# x = "Hello"
# new_x = x.lower()
# new_y = x.capitalize()
# new_z = x.upper()
# print( new_z)

# def print_abs(val):
#     if val < 0:
#         print(0-val)
#     else:
#         print(val)   

# x = print_abs(-2.7)
# print(x)

def inc_val(val):
    val = val+1
x = 7
inc_val(x)
print(x)

def swap(val1, val2):
    tmp = val1
    val1 = val2
    val2 = tmp

x = 6
y = 3
swap(x,y)
print(x,",",y)