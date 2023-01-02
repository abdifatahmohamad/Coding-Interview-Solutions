class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = {}
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        for i, char in enumerate(pattern):
            if char in mapping:
                if mapping[char] != words[i]:
                    return False
            elif words[i] in mapping.values():
                return False
            mapping[char] = words[i]
        return True
        