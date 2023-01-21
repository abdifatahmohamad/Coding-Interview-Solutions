class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen = set(nums)
        unique = 0
        for n in nums:
            if (n - diff) in seen and (n - diff * 2) in seen:
                unique += 1

        return unique