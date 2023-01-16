class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen = set(nums)
        one_time_diff = [(n - diff) for n in nums]
        two_time_diff = [(n - diff * 2) for n in nums]
        unique = 0
        for i in range(len(nums)):
            if one_time_diff[i] in seen and two_time_diff[i] in seen:
                unique += 1

        return unique