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


class Solution(object):
    def fib(self):

        while True:
            num = int(
                input("Please enter how many numbers you want in this series: "))
            first = 0
            second = 1
            if num == 0 or num == 1:
                print(f'Please enter a number that is more than {num}')
            else:
                for number in range(num):
                    print(first, end=' ')
                    # Swap/Shift numbers in the list:
                    temp = first + second
                    first = second
                    second = temp + second

            playAgain = str(
                input("\nDo you want to enter another number of series? (y/n): "))
            if playAgain == 'y':
                continue
            else:
                print("Thank you, maybe later!")
                break


solution = Solution()
solution.fib()
