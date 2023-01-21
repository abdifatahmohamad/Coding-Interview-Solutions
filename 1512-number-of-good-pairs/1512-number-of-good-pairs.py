class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        mapping = {}
        res = 0
        for n in nums:
            if n in mapping:
                res += mapping.get(n)
            mapping[n] = mapping.get(n, 0) + 1

        return res
       
        
        '''
        nums = [1, 2, 3, 1, 1, 3]
        (0, 3) (1, 1)
        (0, 4) (1, 1)
        (3, 4) (1, 1)
        (2, 5) (3, 3)
        '''