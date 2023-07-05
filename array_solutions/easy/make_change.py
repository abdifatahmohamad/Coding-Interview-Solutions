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
print(solution.make_change(33))  # (3, 1, 0, 1)
print(solution.make_change(23))  # (3, 0, 2, 0)


"""
Explanation:

    Let's say n = 33
    dominations = [1, 5, 10, 25]
    dominations[i] = 25
    res = [0, 0, 0, 0]
    n = 33
    33 >= 25 == true
        while 33 - 25 >= 0 == true
            res[3] += 1
            33 - 25 = 8
    res = [0, 0, 0, 1]
    
    Iteration 2:
    n = 8
    dominations[i] = 10
    8 >= 10 == false
    while 8 - 10 >= 0 == false
        the condition is false so nothing happens here
        res[2] += 0
    res = [0, 0, 0, 1]


    Iteration 3:
    n = 8
    dominations[i] = 5
    8 >= 5 == true
    while 8 - 5 >= 0 == true
        res[1] += 1
        8 - 5 = 3
    res = [0, 1, 0, 1]

    Iteration 4:
    n = 3
    dominations[i] = 1
    3 >= 1 == true
    while 3 - 1 >= 0 == true
        res[0] += 1
        3 - 1 = 2
    res = [1, 1, 0, 1]

    n = 2
    dominations[i] = 1
    2 >= 1 == true
    while 2 - 1 >= 0 == true
        res[0] += 1
        2 - 1 = 1
    res = [2, 1, 0, 1]

    n = 1
    dominations[i] = 1
    1 >= 1 == true
    while 1 - 1 >= 0 == true
        res[0] += 1
        1 - 1 = 0
    res = [3, 1, 0, 1]

    n = 0
    dominations[i] = 1
    0 >= 1 == false
    while 0 - 1 >= 0 == true
        the condition is false so nothing happens here

    return res = [3, 1, 0, 1]

    """
