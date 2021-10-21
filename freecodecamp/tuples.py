# Tuples are ordered immutable, allows duplicates

mytuple = ("max", 28, "Boston")
mytuple2 = "David", 30, "Chicago"

print(mytuple)
print(mytuple2)
print(type(mytuple))

# Even if you place it in the brackets it still treats as a string
mytuple3 = ("John")
print(mytuple3)
print(type(mytuple3))

# instead use a ,
mytuple4 = ("John",)
print(mytuple4)
print(type(mytuple4))

mytuple5 = tuple(["David",50,"New York"])
print(mytuple5)
print(type(mytuple5))

print(mytuple5[0])
print(mytuple5[1])
print(mytuple2[2])
# print(mytuple5[5]) IndexError: tuple index out of range

print(mytuple5[-1])
print(mytuple5[-2])
print(mytuple2[-3])

# This is not possible as tuple is immutable
# mytuple5[0] = "Tim"  TypeError: 'tuple' object does not support item assignment
print(" For loop for tuple ")
for val in mytuple5:
    print(val)

if "David1" in mytuple5:
    print("Yes")
else:
    print("NO")

print(len(mytuple5))

mytuple6 = ('a','P','p','l','e')
print(mytuple6.count('p'))
print(mytuple6.index('p'))

converttupletolist = list(mytuple6)
print(converttupletolist)
print(type(converttupletolist))

convertlisttotuple = tuple(converttupletolist)
print(converttupletolist)
print(type(convertlisttotuple))

#Splice works even in the tuple
tuplenumbers = (1,2,3,4,5,6,7,8,9,10)
mysplicetuple = tuplenumbers[4:]
print(tuplenumbers[4:])
print(tuplenumbers[3:5])
print(tuplenumbers[::1])
print(tuplenumbers[::2])
print(tuplenumbers[::-1])

#unpecking placing tuple values to variable -- the items and the count should match
name,age,city = mytuple5
print(name)
print(age)
print(city)
# ww,name,age,city = mytuple5 ValueError: not enough values to unpack (expected 4, got 3)


i1, *i2, i3 = tuplenumbers
print(i1)
print(i2)
print(i3)

import sys
my_list = ["Hello","world",2,3,4,True]
my_tuple = ("Hello","world",2,3,4,True)

# even though both are same, list take more size than that of tuple
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

# even though both are same, list take time than that of tuple
import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))
