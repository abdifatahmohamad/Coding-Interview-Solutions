from typing import List
# Solution 1 using two pointers. Doesn't work in Leetcode coz array
# shouldn't be modified [sorted]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total > target:
                right -= 1
            elif total < target:
                left += 1
            else:
                return [left, right]
        return [-1, -1]

# Solution 2 using hash map


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if num in mapping:
                return [mapping[num], i]
            else:
                mapping[complement] = i

        return [-1, -1]


solution = Solution()
# Array sorted under the hood: [2,7,11,15], 9 => [0, 1]
print(solution.twoSum([2, 11, 7, 15], 9))
