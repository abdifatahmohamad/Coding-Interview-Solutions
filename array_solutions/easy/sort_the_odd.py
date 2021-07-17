# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python
# O(N LOG N) Time || O(N) Space

from typing import List


class Solution:
    def sort_array(self, nums: List[int]) -> List[int]:
        odd_nums = sorted([num for num in nums if num % 2 != 0], reverse=True)
        for i, num in enumerate(nums):
            if num % 2 != 0:
                nums[i] = odd_nums.pop()
        return nums

######################################################
# Another way to solve it:
# O(N LOG N) Time || O(N) Space


class Solution:
    def sort_array(self, nums: List[int]) -> List[int]:
        odd_nums = []
        for i, val in enumerate(nums):
            if val % 2 != 0:
                odd_nums.append(val)
                nums[i] = 'inf'

        odd_nums.sort(reverse=True)
        for i, el in enumerate(nums):
            if el == 'inf':
                nums[i] = odd_nums.pop()
        return nums


solution = Solution()
print(solution.sort_array([5, 8, 6, 3, 4]))  # [3, 8, 6, 5, 4]
# print(solution.sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) # [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
# print(solution.sort_array([7, 1])) # [1, 7]
