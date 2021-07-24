class Solution(object):
    def fib(self, N: int) -> int:
        if (N <= 1):
            return N
        if (N == 2):
            return 1

        first, second = 0, 1
        for i in range(1, N):
            temp = first + second
            first = second
            second = temp
        return second


solution = Solution()
N = 3
print(solution.fib(N))

###############################################
