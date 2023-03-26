class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        '''
        Iterate over nums and ignore non-zero values. When encountering zero value increment res variable by one. 
        Also, keep track of the length (count variable) of how many consecutive zeroes 
        we are seeing and add that to the res. Finally return res.
        '''
        res = count = 0
        for num in nums:
            if num == 0:
                count += 1
                res += count
            else:
                count = 0
        return res
