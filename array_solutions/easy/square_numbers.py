# Three ways to square numbers

# As an array
# def square(arr):
#     for i in range(len(arr)):
#         arr[i] = i * i
#         print(f"The square of {i} is {arr[i]}")
#     return arr
#
#
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# square(arr)


# Using range numbers
# def square(x):
#     for i in range(x):
#         x = i * i
#         print(f"The square of {i} is {x}")
#     return x
#
# square(10)

# Calling square function inside a for loop
def square(x):
    return x * x


for i in range(10):
    print(f"The square of {i} is {square(i)}")
