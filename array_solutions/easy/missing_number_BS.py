from typing import List


# leetcode 268. Missing Number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        left, right = 0, len(nums)

        while left < right:
            mid = (right + left) // 2
            if nums[mid] <= mid:
                left = mid + 1
            else:
                right = mid

        return left
