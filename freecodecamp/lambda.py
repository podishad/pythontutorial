
add10 = lambda x: x+10
print(add10(20))

square_of_numbers = lambda x: x*x
print(square_of_numbers(9))

add_3_num = lambda x,y,z: x+y+z
print(add_3_num(10,50,100))

points2D = [(1, 9), (4, 1), (5, -3), (10, 2)]
points2D_sorted = sorted(points2D)
print(points2D_sorted)

points2D_sorted = sorted(points2D, key = lambda x:x[1])
print(points2D_sorted)

def sort_function_with_second_param(x):
    return x[1]

points2D_sorted = sorted(points2D, key = sort_function_with_second_param)
print(points2D_sorted)

# Sorting by sum of each tuple
points2D_sorted_by_sum = sorted(points2D, key= lambda x: x[0]+x[1])
print(points2D_sorted_by_sum)


# Lambda with MAP function
a = [1,2,3,4,5,6,7]
b = map(lambda x:x*x, a)
print(list(b))

# Below is list comprehensive
b = [x*x for x in a]
print(b)


#lambda with filter function
b = filter(lambda x: x%2 == 0, a)
print(list(b))

b = [ x for x in a if x%2 == 0]
print(b)


# Reduce function with lambda
from functools import reduce
multiplication = reduce(lambda x,y: x*y, a)
print(multiplication)