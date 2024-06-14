class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        mapping = {}
        for n in nums:
            if n % 2 == 0:
                mapping[n] = mapping.get(n, 0) + 1
        
        if not mapping:
            return -1 
        
        max_freq = max(mapping.values())
        res = float("Inf")
        for k, v in mapping.items():
            if v == max_freq:
                res = min(res, k)
               
        return res
        