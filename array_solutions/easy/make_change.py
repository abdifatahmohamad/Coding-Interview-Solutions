"""
Given a number of cents, write a function to make change with the fewest number of coins,
returning the number of coins for each denomination needed for the given number of cents.

The coins can be of the standard U.S. denominations: (1, 5, 10, 25).

Example: `make_change(33) -> (3, 1, 0, 1)`

i.e., `33 cents = 3*1 + 1*5 + 0*10 + 1*25`

make_change(23) --> (3, 0, 2, 0)
"""


class Solution:
    # Solution 1:
    '''

    def make_change(self, n):
        res = []
        quarters = n // 25
        remainder = n % 25

        dime = remainder // 10
        remainder = remainder % 10

        five_cents = remainder // 5
        remainder = remainder % 5

        last = remainder

        res.append((last, five_cents, dime, quarters))

        return res

        '''

    # Solution 2:
    def make_change(self, n):
        denominations = [1, 5, 10, 25]
        res = [0 for _ in range(len(denominations))]
        for i in range(len(denominations) - 1, -1, -1):
            if n >= denominations[i]:

                while n - denominations[i] >= 0:
                    res[i] += 1
                    n -= denominations[i]

        return res


solution = Solution()
print(solution.make_change(200))  # (3, 1, 0, 1)
print(solution.make_change(23))  # (3, 0, 2, 0)
