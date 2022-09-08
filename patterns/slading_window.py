'''
Given two strings `s1` and `s2`, return `true` *if* `s2` *contains a permutation of* `s1`*, or* `false` *otherwise*.
In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.


Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

'''
from collections import Counter, defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        window = defaultdict(int)
        for i, c in enumerate(s2):
            window[c] += 1
            if i >= len(s1):
                left = s2[i - len(s1)]
                if window[left] == 1:
                    del window[left]
                else:
                    window[left] -= 1
            if s1_counter == window:
                return True
        return False


solution = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(solution.checkInclusion(s1, s2))
