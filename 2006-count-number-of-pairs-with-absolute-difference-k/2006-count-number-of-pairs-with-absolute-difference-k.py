class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        mapping = {}
        for n in nums:
            mapping[n] = mapping.get(n, 0) + 1

        count = 0
        for n in nums:
            if n + k in mapping:
                count += mapping[n + k]
        return count

        