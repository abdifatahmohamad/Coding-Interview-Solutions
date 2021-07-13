from typing import List

# 1480. Running Sum of 1d Array LEETCODE


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return

        result = [0] * len(nums)
        # result[0] = nums[0]

        for i in range(len(nums)):
            # for i in range(1, len(nums)):
            # Check i
            if i == 0:
                result[0] = nums[0]
            curr = nums[i]
            prev = result[i - 1]
            total = curr + prev
            result[i] = total
        return result


solution = Solution()
print(solution.runningSum([1, 1, 1, 1]))  # [1, 2, 3, 4]
print(solution.runningSum([1, 2, 3, 4]))  # [1, 3, 6, 10]
