class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(sub):
            char_count = {}
            for char in sub:
                char_count[char] = char_count.get(char, 0) + 1

            for char in char_count:
                if char.islower() and char.upper() not in char_count:
                    return False
                if char.isupper() and char.lower() not in char_count:
                    return False

            return True
    
        n = len(s)
        max_length = 0
        max_start = 0
        max_end = 0

        for l in range(n):
            r = l + 1
            while r <= n:
                substring = s[l:r]
                if is_nice(substring) and len(substring) > max_length:
                    max_length = len(substring)
                    max_start = l
                    max_end = r
                r += 1

        return s[max_start:max_end]
    
 








        