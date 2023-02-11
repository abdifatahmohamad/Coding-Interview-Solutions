class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        mapping = {}
        for i, n in enumerate(nums):
            mapping[n] = i

        max_val = float("-Inf")
        for k in mapping.keys():
            if -k in mapping:
                max_val = max(max_val, k)
    
        return max_val if max_val != float("-Inf") else -1
            
        