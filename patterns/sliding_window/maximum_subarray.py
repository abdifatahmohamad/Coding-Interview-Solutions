'''
# Sliding window technique called "fixed size/length window or fixed variant:
Find maximum sum of contiguous subarray of size 3 (fixed window size of 3)
nums = [4, 2, 2, 7, 8, 1, 2, 8, 10]
k = 3
Output: 16
Explanation: The max sum of window size of 3 that we can get from the input are 7 + 8 + 1 = 16
https://www.youtube.com/watch?v=MK-NZ4hN7rs&t=1555s
'''


class Solution:
    def maximum_subarray(self, nums, k) -> int:
        max_value = float("-Inf")
        curr_running_sum = 0
        for i in range(len(nums)):
            curr_running_sum += nums[i]
            if i >= k - 1:
                max_value = max(max_value, curr_running_sum)
                curr_running_sum -= nums[i - (k - 1)]

        return max_value


solution = Solution()
nums = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
print(solution.maximum_subarray(nums, 3))
