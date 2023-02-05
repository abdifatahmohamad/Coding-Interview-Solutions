class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        target = 9
        nums = [2, 15, 11, 7]
        comp = 9 - 2 = 7
        comp = 9 - 15 = -6
        comp = 9 - 11 = -2
        comp = 9 - 7 = 2
        2 in mapping yes, return mapping[complement] which is 2:0 --> index 0 and i which is current index of 3


        mapping = {
        2: 0,
        15: 1,
        11: 2
        }
        
        '''
        mapping = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement not in mapping:
                mapping[n] = i
            else:
                return [mapping[complement], i]
        return [-1, -1]