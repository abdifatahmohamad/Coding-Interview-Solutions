from typing import List
import collections


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        mapping = collections.Counter(nums)
        freq = missing = 0
        for i in range(1, len(nums) + 1):
            if i not in mapping:
                missing = i
            if mapping[i] > 1:
                freq = i

        return [freq, missing]


solution = Solution()
print(solution.findErrorNums([1, 2, 2, 4]))  # [2, 3]
