

mylist = ["banana", "apple" , "strawberry", "grape"]
print(mylist)

if( "apple" in mylist):
    print("Yes apple exits")
else:
    print("No it doesnt have an apple")

print(len(mylist))
mylist.append("kiwi")
print(mylist)

mylist.insert(1, "water melon")
print(mylist)

mylist.remove("kiwi")
print(mylist)
mylist.sort()
print(mylist)
mylist.reverse()
print(mylist)

my_sorted_list = sorted(mylist)
print(my_sorted_list)
print("my current list is ")
print(mylist)
print(mylist[1:4])
print(mylist[1:])
print(mylist[:5])

mynumberslist = [1,2,3,4,5,6,7,8,9,10]
print(mynumberslist)
# STEP INDEX
print(mynumberslist[::1])
print(mynumberslist[::2])
print(mynumberslist[::3])
print(mynumberslist[::-1])
print(mynumberslist[::-2])


print(mynumberslist)
mynewnumberslistcopy = mynumberslist
print(mynumberslist)
print(mynewnumberslistcopy)

mynewnumberslistcopy.append(999)
# In the memory both are pointing to the same array. We have to be very careful when copying use .copy()
print(mynumberslist)
print(mynewnumberslistcopy)

# As we used .copy on that array it is not referring to the same array in the memory anymore
mynewnumberslistcopy2 = mynumberslist.copy()
# list(mynumberlist)   mynumberslist[:]
# These above are pretty much similar as .copy method
mynewnumberslistcopy2.append(666)
print(mynewnumberslistcopy2)
print(mynumberslist)

squaredmynumberslist = [i*i for i in mynumberslist]
print(squaredmynumberslist)

cubemynumberslist = [i*i*i for i in mynumberslist]
print(cubemynumberslist)