class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        mapping = {}
        for i in range(1, len(nums)):
            prev, curr = nums[i - 1], nums[i]
            total = curr + prev
            if total in mapping:
                return True
            mapping[total] = True
        return False
