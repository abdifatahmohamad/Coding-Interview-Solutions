class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        mapping = {}  
        res = 1
        i = j = 0
        while i < len(nums) and j < len(nums):
            mapping[nums[j]] = mapping.get(nums[j], 0) + 1
            while mapping[nums[j]] > k:
                mapping[nums[i]] -= 1
                i += 1
            res =  max(res, j - i + 1)
            j += 1
            
        return res
            
        