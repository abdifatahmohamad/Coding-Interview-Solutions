from typing import List


class Solution:
    def match_words(self, words: List[int]) -> List[int]:
        count = 0
        for word in words:
            if len(word) > 1 and word[0] == word[-1]:
                count += 1
        return count


solution = Solution()
# 'aba', '1221' => 2
print(solution.match_words(['abc', 'xyz', 'aba', '1221']))  # Output: 2
