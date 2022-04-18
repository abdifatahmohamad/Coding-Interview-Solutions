# https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        mapping = {}
        for ch in s:
            mapping[ch] = mapping.get(ch, 0) + 1

        for ch in t:
            if ch not in mapping or mapping[ch] < 1:
                return ch
            else:
                mapping[ch] -= 1

        return -1


# This is same as "valid anagram problem", same data structure involved:
# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for char in s:
            seen[char] = 1 + seen.get(char, 0)

        for letter in t:
            if letter not in seen or seen[letter] < 1:
                return False
            else:
                seen[letter] -= 1

        return True
