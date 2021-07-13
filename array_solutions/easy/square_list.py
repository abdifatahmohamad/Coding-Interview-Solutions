# Square list using fixed list size

from typing import List


class Solution:
    def square_list(self, nums: List[int]) -> List[int]:
        square = [0] * len(nums)
        for i in range(len(nums)):
            square[i] = nums[i] ** 2
        return square


solution = Solution()
print(solution.square_list([3, 7, 4, 6, 1, 8, 2]))  # [9, 49, 16, 36, 1, 64, 4]
print(solution.square_list([3, 7]))  # [9, 49]
