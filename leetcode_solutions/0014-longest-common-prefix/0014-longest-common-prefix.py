class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        longest_prefix = ""
        for i in range(len(s[0])):
            ch = s[0][i]
            for j in range(1, len(s)):
                if i >= len(s[j]) or s[j][i] != ch:
                    return longest_prefix
            longest_prefix += ch

        return longest_prefix
        