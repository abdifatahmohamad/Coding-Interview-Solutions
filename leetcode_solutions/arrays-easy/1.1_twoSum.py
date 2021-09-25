from typing import List
# Solution 1 using two pointers. Doesn't work in Leetcode coz array
# shouldn't be modified [sorted]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Array sorted started at index 0
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
def twoSum(nums, target):
    seen = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement not in seen:
            seen[nums[i]] = i
        else:
            return [seen[complement], i]
    return seen


print(sum([2, 15, 11, 7], 9))

# Complement = target - num
# 9 - 2 = 7 -> is 7 in seen => NO, store 2 in hashmap
# 9 - 15 = -6 -> is -6 in seen => NO, store 15 in hashmap
# 9 - 11 = -2 -> is -2 in seen => NO, store 11 in hashmap
# 9 - 7 = 2 -> is 2 in seen => YES, return it its index in hashmap and the index of nums[i]

# seen = {
# 2 = 0
# 15  = 1
# 11 - 2
# }

# Loop through till the end of numbers array
# determine complement
# if complement is in dictionary, return value of complement and i
# otherwise, new key-value pair in dicitonary, number -> i


solution = Solution()
# Array sorted under the hood: [2,7,11,15], 9 => [0, 1]
print(solution.twoSum([2, 11, 7, 15], 9))
