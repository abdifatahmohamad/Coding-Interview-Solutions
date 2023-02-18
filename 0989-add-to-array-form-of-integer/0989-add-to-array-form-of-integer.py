class Solution:
    def addToArrayForm(self, nums: List[int], k: int) -> List[int]:
        nums = ''.join(str(num) for num in nums)
        digits = int(nums) + k
        return [int(d) for d in str(digits)]
        