'''
List:
1. Can contain Heterogeneous element
Mutable : value can be changed

'''

# Heterogeneous
nums = [1,2,3,4,5, "A", "B", "C"]

# Mutable
nums.append("D")
print(nums)

nums.insert(2,2)
print(nums)

nums.remove(2)          # give value to be removed , only last value will be removed if duplicate
print(nums)

nums.pop(3)            # give index to be removed
print(nums)

nums.pop()            # last value can be removed

del nums[2:]             # delete multiple values togeteher

nums.extend([1,2,3,"f"])        # add multiple value together
print(nums)

# there are other default function as well such as min, max, sum etc

