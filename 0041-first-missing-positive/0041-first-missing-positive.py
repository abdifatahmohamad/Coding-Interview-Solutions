class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mapping = {}
        for num in nums:
            if num > 0:
                mapping[num] = True
        missing = 1
        while missing in mapping:
            missing += 1

        return missing
