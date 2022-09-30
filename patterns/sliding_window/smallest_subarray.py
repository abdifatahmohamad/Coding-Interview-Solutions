'''
# Sliding window technique called "dynamically resizable windows or dynamic variant:
Find smallest subarray with given sum, where sum of value >= to the target sum

Test Case 1:
nums = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
target_sum = 8
Output: 1

Explanation: The smallest sum that is >= to the target sum from the input is 8 which is only 1 value. Note we have another 8 which >= to the target sum but return only the first value that is >= to the target sum.

Test Case 2:
nums = [2, 7, 0]
target_sum = 9
Output: 2

Explanation: 2 + 7 >= 9, hence the output should be 2

https://www.youtube.com/watch?v=MK-NZ4hN7rs&t=1555s
'''


class Solution:
    def smallest_subarray(self, nums, target) -> int:
        min_value = float("Inf")
        curr_running_sum = 0
        left = 0
        for right in range(len(nums)):
            curr_running_sum += nums[right]
            while curr_running_sum >= target:
                min_value = min(min_value, (right - left + 1))
                curr_running_sum -= nums[left]
                left += 1
        return min_value


solution = Solution()
nums = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
print(solution.smallest_subarray(nums, 8))
