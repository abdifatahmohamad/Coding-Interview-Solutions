class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        mapping = {}
        for i, n in enumerate(nums):
            mapping[n] = i

        max_val = float("-Inf")
        for k in mapping.keys():
            if k > 0 and -k in mapping:
                max_val = max(max_val, k)
    
        if max_val == float("-Inf"):
            return -1
        else:
            return max_val
            
        