class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        res = ""
        for i in range(len(s)):
            # setup pointers
            l, r = expand_odd_length(s, i, i)
            # Check the length of the palindrome
            if (r - l + 1) > max_length:
                # Update the result
                res = s[l: r + 1]
                # Update max length
                max_length = r - l + 1

            # setup pointers
            l, r = expand_even_length(s, i, i + 1)
            # Check the length of the palindrome
            if (r - l + 1) > max_length:
                # Update the result
                res = s[l: r + 1]
                # Update max length
                max_length = r - l + 1
        return res

# Helper function that checks odd length palindrome
def expand_odd_length(s, l, r):
    # while l and r are in bound, and it's palindrome (l and r are equal)
    while l >= 0 and r < len(s) and s[l] == s[r]:
        # Expand pointers
        l -= 1
        r += 1
    return l + 1, r - 1

# Helper function that checks even length palindrome
def expand_even_length(s, l, r):
    # while l and r are in bound, and it's palindrome (l and r are equal)
    while l >= 0 and r < len(s) and s[l] == s[r]:
        # Expand pointers
        l -= 1
        r += 1
    return l + 1, r - 1
        