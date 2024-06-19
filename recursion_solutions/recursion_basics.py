
# Reference: https://www.youtube.com/watch?v=un6PLygfXrA&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=3

# Print name Abdi five times
# def foo(count):
#     if count == 5:
#         return
    
#     print("Abdi")
#     return foo(count + 1)

# if __name__ == "__main__":
#     foo(0)


# def foo(i, n):
#     if i >= n:
#         return
#     print("Abdi")
#     foo(i + 1, n)

# if __name__ == "__main__":
#     n = int(input("Enter the number of times to print name: "))
#     foo(0, n)

# Print number 1 to N
# def foo(i, n):
#     if i > n:
#         return
#     print(i)
#     foo(i + 1, n)

# if __name__ == "__main__":
#     n = int(input("Enter the number to print 1 -> N reverse: "))
#     foo(1, n) # 1, 2, 3 ... and so on

# Print number in reverse order N to 1
# def foo(i, n):
#     if i < 1:
#         return
#     print(i)
#     foo(i - 1, n)

# if __name__ == "__main__":
#     n = int(input("Enter the number to print 1 -> N reverse: "))
#     foo(n, n) # whatever n happens to be ... 3, 2, 1

# Print 1 to N using backtracking
# def backtrack(i, n):
#     if i < 1:
#         return
#     backtrack(i - 1, n)
#     print(i) # Pay attention print i after function call here

# if __name__ == "__main__":
#     n = int(input("Enter the number to print 1 -> N backtrack: "))
#     backtrack(n, n) # 1, 2, 3 ... and so on

# Print N to 1 using backtracking
def backtrack(i, n):
    if i > n:
        return
    backtrack(i + 1, n)
    print(i)

if __name__ == "__main__":
    n = int(input("Enter the number to print 1 -> N backtrack: "))
    backtrack(1, n) # whatever n happens to be ... 3, 2, 1