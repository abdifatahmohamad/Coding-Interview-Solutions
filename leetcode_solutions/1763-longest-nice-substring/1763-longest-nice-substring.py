class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        max_length = 0
        max_start = 0
        max_end = 0

        for l in range(n):
            r = l + 1
            while r <= n:
                substring = s[l:r]
                if self.is_nice(substring) and len(substring) > max_length:
                    max_length = len(substring)
                    max_start = l
                    max_end = r
                r += 1

        return s[max_start:max_end]
    
    
    # Helper method
    def is_nice(self, s):
        unique = set(s)
        for ch in unique:
            if ch.lower() not in unique or ch.upper() not in unique:
                return False
        return True
    
 








        