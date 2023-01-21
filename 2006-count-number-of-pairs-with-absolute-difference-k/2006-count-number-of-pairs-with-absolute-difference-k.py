class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        mapping = Counter(nums)

        count = 0
        for n in nums:
            complement = n + k
            if complement in mapping:
                count += mapping[complement]
        return count

        