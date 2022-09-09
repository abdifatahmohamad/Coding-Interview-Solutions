class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        longest = l = 0
        for r, ch in enumerate(s):
            if ch in window:
                if window[ch] >= l:
                    l = window[ch] + 1
            longest = max(longest, r - l + 1)
            window[ch] = r

        return longest
        