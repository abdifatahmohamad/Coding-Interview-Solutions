class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0 for _ in range(len(nums))]
        left, right = 0, len(nums) - 1
        i = len(nums) - 1
        while i >= 0:
            if abs(nums[left]) < abs(nums[right]):
                result[i] = nums[right] * nums[right]
                right -= 1
            else:
                result[i] = nums[left] * nums[left]
                left += 1
            i -= 1

        return result
    
    
   
        