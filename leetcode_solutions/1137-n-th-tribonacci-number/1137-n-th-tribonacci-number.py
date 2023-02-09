class Solution:
    # dict = {0:0,1:1,2:1}
    def tribonacci(self, n: int, fibMemo = {0: 0, 1: 1, 2: 1}) -> int:
        if n < 3:
            return fibMemo[n]
        
        elif n in fibMemo:
            return fibMemo[n]
        
        fibMemo[n] = self.tribonacci(n - 3, fibMemo) + \
                     self.tribonacci(n -  2, fibMemo) + \
                     self.tribonacci(n - 1, fibMemo)
        return fibMemo[n]
        
        
        
        
        # You can use memoization to optimize this function by storing previously calculated values in a           dictionary and reusing them instead of recalculating
        '''
        fibMemo = {0: 0, 1: 1, 2: 1}
        if n < 3:
            return fibMemo[n]
        if n in fibMemo:
            return fibMemo[n]

        fibMemo[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        return fibMemo[n]
        
        '''