from collections import Counter

value1 = "aaaaabbbbbbcccccccddde"
mycollec1 = Counter(value1)
print(mycollec1)
print(mycollec1.keys())
print(mycollec1.values())


from collections import namedtuple
mytuple = namedtuple('MyPoint',['a','b'])
mytupleIs = mytuple(10,20)
print(mytupleIs)
print(mytuple)
print(mytupleIs.a)
print(mytupleIs.b)
