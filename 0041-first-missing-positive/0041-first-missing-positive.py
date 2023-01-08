class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        missing = 1
        for i in range(len(nums)):
            if nums[i] == missing:
                missing += 1
            elif nums[i] > missing:
                return missing
        return missing
        