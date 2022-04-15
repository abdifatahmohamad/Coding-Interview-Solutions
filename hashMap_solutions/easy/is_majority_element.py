# https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/
from ast import List


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        mapping = {}
        for n in nums:
            mapping[n] = 1 + mapping.get(n, 0)

        if target in mapping:
            count = mapping.get(target)
        else:
            count = 0

        return count > len(nums) // 2
