# Recursion happens when function is called within itself.
def recursion(n):
    if n == 1:
        return n
    else:
        return recursion(n - 1)


print(recursion(10))


# Iteratively
def func(n):
    stack = []
    for i in range(n - 1, -1, -1):
        if i == 1:
            return i
        else:
            stack.append(i - 1)


print(func(10))


# Print all positive even numbers smaller or equal to 8
def even_numbers(num):
    print(num, end=", ")
    if num % 2 != 0:
        print("Please enter an even number.")
    elif num == 2:
        return num
    else:
        return even_numbers(num - 2)


print(even_numbers(8))
