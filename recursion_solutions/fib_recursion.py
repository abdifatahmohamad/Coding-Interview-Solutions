# Reference: https://www.youtube.com/watch?v=kvRjNm4rVBE&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=5

# Multiple Recursion Calls
# TC = ~ 2 ^ n AKA (exponential)
def fib(i):
    # Base case:
    if i <= 1: # It holds the first 2 fibonacci numbers which are [0,1]
        return i
    else:
        return fib(i - 1) + fib(i - 2)

if __name__ == "__main__":
    N = 8 # 0, 1, 1, 2, 3, 5, 8, 13 ====> 8 + 13 = 21
    print(fib(N))