from itertools import product

a = [1,2]
b = [3,4]

prod =  product(a,b)
print(prod)
prod = list(prod)
print(prod)

from itertools import groupby
a = [1,2,3,4,5]

def smaller_than_3(x):
    return x<4

def odd_or_even(x):
    if x%2 == 0:
        return "EVEN"
    else:
        return  "ODD"

group_obj = groupby(a, key=smaller_than_3)
for key,value in group_obj:
    print(key, list(value))

group_obj = groupby(a, key=odd_or_even)
for key,value in group_obj:
    print(key, list(value))

group_obj = groupby(a, key = lambda x: x<3)
for key,value in group_obj:
    print(key, list(value))

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]


group_obj = groupby(persons, lambda x: x['age'])
for key,value in group_obj:
    print(key, list(value))

