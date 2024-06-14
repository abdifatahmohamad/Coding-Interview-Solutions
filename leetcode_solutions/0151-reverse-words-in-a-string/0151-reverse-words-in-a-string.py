class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string
        s = s.split()
        # Convert string into a list
        words = list(s)
        left, right = 0, len(words) - 1
        while left < right:
            # Swap words
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        # Convert list back to string
        return " ".join(s)
        