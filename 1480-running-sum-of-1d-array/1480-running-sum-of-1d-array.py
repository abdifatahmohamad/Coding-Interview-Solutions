class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return
        
        result = [nums[0]]
        for i in range(1, len(nums)):
            total = nums[i] + result[-1]
            result.append(total)
            
        return result