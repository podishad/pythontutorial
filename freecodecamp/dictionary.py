
# Dictionary: Keys-Value paris, mutable, Unordered
dict1 = {"name":"John", "age":30,"city":"San Jose"}
print(dict1)

# dict is used to create a dictionary where keys doesnt need to provide in the double quotes
dict2 = dict(name="Leo", age = 50, city="Chicago")
print(dict2)

print(dict1["name"])
print(dict2["name"])
dict2["email"] = "abc@gmail.com"
print(dict2)

del dict2["name"]
print(dict2)

dict2.pop("city")
print(dict2)

dict2.popitem()
print(dict2)

if "name" in dict1:
    print(dict1["name"])

try:
    print(dict1["lastname"])
except:
    print("LastName not found")

# For loop keys
for key in dict1:
    print(key)

#for keys as specific
for key in dict1.keys():
    print(key)

#for values as specific
for value in dict1.values():
    print(value)

#Print both key and a value
print("Print both key and value")
for key, value in dict1.items():
    print(key, value)

# To copy use .copy / dict(____)
# to update use dict1.update(dict2)
dict2.update(dict1)

print(dict2)

mytuple = (1,4)
dict_by_tupple = {mytuple: 5}
print(dict_by_tupple)
