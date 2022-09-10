'''
# Sliding window technique called "dynamically resizable windows or dynamic variant:
Find smallest subarray with given sum, where sum of value >= to the target sum
nums = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
target_sum = 8
Output: 1
Explanation: The smallest sum that is >= to the target sum from the input is 8 which is only 1 value. Note we have another 8 and 10 which >= to the target sum but return only the first value.
https://www.youtube.com/watch?v=MK-NZ4hN7rs&t=1555s
'''


class Solution:
    def smallest_subarray(self, nums, target) -> int:
        min_window_size = float("Inf")
        curr_window_sum = 0
        left = 0
        for right in range(len(nums)):
            curr_window_sum += nums[right]
            while curr_window_sum >= target:
                min_window_size = min(min_window_size, (right - left + 1))
                curr_window_sum -= nums[left]
                left += 1
        return min_window_size


solution = Solution()
nums = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
print(solution.smallest_subarray(nums, 8))
