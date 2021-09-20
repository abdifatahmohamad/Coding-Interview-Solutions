# Three ways to create an empty fixed array size:

# Solution 1:
# array = [0] * 10
# for i in range(len(array)):
#     array[i] = None
# print(array)

# Solution 2 - Using list comprehension:
# array = [None for _ in range(10)]
# print(array)

# Solution 3:
size = 10
array = [None] * size
print(array)
