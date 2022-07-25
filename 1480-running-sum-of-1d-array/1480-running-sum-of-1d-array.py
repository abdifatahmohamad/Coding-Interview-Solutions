class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return
        
        result = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                result[0] = nums[0]
            
            curr = nums[i]
            prev = result[i - 1]
            total =  curr + prev
            result[i] = total
            
        return result