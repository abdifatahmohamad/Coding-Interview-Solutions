class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        mapping = collections.Counter(nums)
        
        total = 0
        for k, v in mapping.items():
            if v == 1:
                total += k
        return total
        