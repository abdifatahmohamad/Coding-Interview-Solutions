from typing import List


# Brute Force Solution O(n^2) Time || O(1) Space
class Solution:
    def nextGreaterElement(self, nums: List[int]) -> List[int]:
        ans = [-1] * (len(nums))
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    ans[i] = nums[j]
                    break
        return ans


solution = Solution()
# nums = [11, 13, 21, 3]
nums = [9, 1, 20, 2, 8, 6, 4, 2]

# Output: [13 ,21, -1, -`1]
# Output: [20, 20, -1, 8, -1, -1, -1, -1]
print(solution.nextGreaterElement(nums))
