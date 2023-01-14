# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         lookup = Counter(nums)
#         missing = 0
#         for i in range(1, len(nums) + 1):
#             if i not in lookup:
#                 missing = i

#         return missing
    

    
class Solution:
    def missingNumber(self, nums):
        mp = {n: i for i, n in enumerate(nums)}
            
        for i in range(len(nums)+1):
            if i not in mp:
                return i
        return 0