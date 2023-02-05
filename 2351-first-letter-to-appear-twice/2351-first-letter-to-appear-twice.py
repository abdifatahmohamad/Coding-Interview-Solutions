class Solution:
    def repeatedCharacter(self, s: str) -> str:
        mapping = {}
        for ch in s:
            if ch in mapping:
                return ch
            else:
                mapping[ch] = 1
        return None
        