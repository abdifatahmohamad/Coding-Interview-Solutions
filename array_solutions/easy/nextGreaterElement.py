from typing import List


# Brute Force Solution O(N) Time || O(1) Space
class Solution:
    def nextGreaterElement(self, nums: List[int]) -> List[int]:
        ans = [0] * (len(nums))
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    ans[i] = nums[j]
                    break
        return ans


##########################################################
# Optimal Solution O(N) Time || O(N) Space Using stack DS

class Solution:
    def nextGreaterElement(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)

        # create an empty stack
        stack = []

        # do for each element
        for i in range(len(nums)):

            # loop till we have a greater element on top or stack becomes empty.

            # Keep popping elements from the stack smaller than the current
            # element, and set their next greater element to the current element
            while stack and nums[stack[-1]] < nums[i]:
                res[stack[-1]] = nums[i]
                stack.pop()

            # push current "index" into the stack
            stack.append(i)

        return res


solution = Solution()
nums = [11, 13, 21, 3]
# Output: [13 ,21, -1, -`1]
print(solution.nextGreaterElement(nums))
