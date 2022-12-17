class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_val = float("Inf")
        l = running_sum = 0
        for r in range(len(nums)):
            running_sum += nums[r]
            while running_sum >= target:
                min_val = min(min_val, r - l + 1)
            
                running_sum -= nums[l]
                l += 1
        return min_val if min_val <= len(nums) else 0
        