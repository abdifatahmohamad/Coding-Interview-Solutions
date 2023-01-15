class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        unique = 0
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                for k in range(2, len(nums)):
                    if (i < j < k) and \
                            (nums[j] - nums[i] == diff) and \
                            (nums[k] - nums[j] == diff):
                        unique += 1
        return unique
        