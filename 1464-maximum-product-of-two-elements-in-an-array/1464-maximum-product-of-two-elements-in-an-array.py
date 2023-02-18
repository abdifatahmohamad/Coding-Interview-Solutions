class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        num1 = float('-inf')
        num2 = float('-inf')

        # Loop through the list and update the maximum values as necessary
        for num in nums:
            if num > num1:
                num2 = num1
                num1 = num
            elif num > num2:
                num2 = num
        max_val = (num1 - 1) * (num2 - 1)
        return max_val
#
        