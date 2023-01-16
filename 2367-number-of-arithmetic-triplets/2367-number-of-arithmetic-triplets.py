class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        mapping = Counter(nums)
        unique = 0
        for n in nums:
            if ((n - diff) in mapping) and ((n + diff) in mapping):
                unique += 1
        return unique