# lambda function

# traditional way
def add(a,b):
    return a+b

val = add(5,6)
print(val)

# lambda function
total = lambda a,b : a+b
print(total(5,6))


# Filter
# function should return True or False
# traditional way

nums = [1,2,3,4,5,6,7,8]
def is_even(n):
    return n%2 == 0

even_num = list(filter(is_even, nums))
print(even_num)

# using lambda

even_num_lam = list( filter(lambda n : n%2 == 0, nums))
print(even_num_lam)

# Map
# function should return the updated value to each element

# Traditional
def update(n):
    return n + 5

update_map_value = list(map(update, even_num))
print(update_map_value)

#using lambda

update_map_value_lam = list(map(lambda n : n + 5, even_num))
print(update_map_value_lam)

#Reduce
# function should return the final value

from functools import reduce

#traditional way
def addAll(a,b):
    return a + b

reduced_val = reduce(addAll, update_map_value_lam)
print(reduced_val)

# using lambda
reduced_val_lam = reduce(lambda a,b : a+b , update_map_value_lam)
print(reduced_val_lam)


