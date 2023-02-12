# Brute force solution, very slow:
def climbStairs(n):
    if n == 0:
        return 1
    if n < 0:
        return 0

    return climbStairs(n - 1) + climbStairs(n - 2)


# Solution of memoization, time Limit Exceeded input of 38
def climbStairs(n):
    memo = {0: 1, 1: 1}
    if n not in memo:
        memo[n] = climbStairs(n - 1) + climbStairs(n - 2)
    return memo[n]


# Fast and optimal solution
def climbStairs(n):
    cache = [0] * (n + 1)
    cache[0] = 1
    cache[1] = 1
    for i in range(2, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[n]


print(climbStairs(38))
