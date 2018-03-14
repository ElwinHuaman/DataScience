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

# def inc_val(val):
#     val = val+1
# x = 7
# inc_val(x)
# print(x)

# def swap(val1, val2):
#     tmp = val1
#     val1 = val2
#     val2 = tmp

# x = 6
# y = 3
# swap(x,y)
# print(x,",",y)

#### METHODS STRIP, SPLIT
# s = '   Extrassss como \n'
# print(s.strip())

# t = "Let\'s split the word"
# u = "vamos a,comer cuando lo sepamos, y si no"
# print(t.split(" "))
# print(u.split(","))

#### SLICING, FIND

# word = 'Hello'
# print(word[1:3])
# print(word[4:8])
# print(word[-4:-1])

# print('HE' in word)
# print(word.find('l'))

#### CASTING, STR, INT, FLOAT

# word = 1
# print(str(word), float(word))

#### LIST, FOR, RANGE, APPEND, POP(delete for index), REMOVE
list = [11,22,33,44]
list2 = [55,66,77,88]
list3 = [99,111]
list[1] = 55
# print(list)
# print(list[2])

# for i in list:
#     print(i)

# list.append(66)
# list.pop(1)
# for i in range(0,len(list)):
#     print(list[i])
# list.remove(11)
# print(list)
# list.extend(list2)
# print(list)
# list.append(list3)
# print(list)

#### METHOD ZIP
for x,y in zip(list, list3):
    print(x," , ",y)