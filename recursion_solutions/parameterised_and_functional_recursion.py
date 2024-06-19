# Reference: https://www.youtube.com/watch?v=un6PLygfXrA&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=3

# Summation of first N numbers using parameterised way
# def parameterised(i, total):
#     if i < 1:
#         print(total)
#         return
#     parameterised(i - 1, total + i)

# if __name__ == "__main__":
#     n = 3
#     total = 0
#     parameterised(n, total) # sum all numbers, if n = 3; 1+2+3 = 6

# Summation of first N numbers using functional way; you need the function return something
# def functional(n):
#     if n == 0:
#         return 0
#     return n + functional(n - 1)

# if __name__ == "__main__":
#     n = 3
#     print(functional(n)) # sum all numbers, if n = 3; 1+2+3 = 6

# Fuctorial of N ==> n = 4, 1 * 2 * 3 * 4 = 24
def functional(n):
    if n == 0:
        return 1
    return n * functional(n - 1)

if __name__ == "__main__":
    n = 4
    print(functional(n)) # sum all numbers, if n = 3; 1+2+3 = 6