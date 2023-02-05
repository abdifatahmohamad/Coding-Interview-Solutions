class Solution:
    def repeatedCharacter(self, s: str) -> str:
        mapping = {}
        for ch in s:
            if ch not in mapping:
                mapping[ch] = 1
            else:
                return ch
        return None
        