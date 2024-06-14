class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        mapping = {}  
        res = 1
        i = 0
        for j in range(len(nums)):
            mapping[nums[j]] = mapping.get(nums[j], 0) + 1
            while mapping[nums[j]] > k:
                mapping[nums[i]] -= 1
                if mapping[nums[i]] == 0:
                    del mapping[nums[i]]
                i += 1
            res =  max(res, j - i + 1)
            j += 1     
        return res
            
        