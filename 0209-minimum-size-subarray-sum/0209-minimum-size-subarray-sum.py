class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_val = float("Inf")
        running_sum = 0
        left = 0
        for right in range(len(nums)):
            running_sum += nums[right]
            while running_sum >= target:
                min_val = min(min_val, right - left + 1)
                running_sum -= nums[left]
                left += 1
     
        return min_val if min_val <= len(nums)  else 0
        