class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        res = ""
        for i in range(len(s)):
            # 1. Take care of odd length palindrome
            l = r = i
            # while l and r are in bound, and it's palindrome (l and r are equal)
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Check the length of the palindrome
                if (r - l + 1) > max_length:
                    # Update the result
                    res = s[l: r + 1]
                    # Update max mlength
                    max_length = r - l + 1
                # Expand pointers
                l -= 1
                r += 1

            # 2. Take care even length palindromes
            l, r = i, i + 1
            # while l and r are in bound, and it's palindrome (l and r are equal)
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Check the length of the palindrome
                if (r - l + 1) > max_length:
                    # Update the result
                    res = s[l: r + 1]
                    # Update max mlength
                    max_length = r - l + 1
                # Expand pointers
                l -= 1
                r += 1
        return res
        