class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        found_last_word = False
        for i in range(len(s) -1, -1, -1):
            char = s[i]
            if char != " ":
                # If a non-space character is found and we haven't found the last word yet, increment the length
                if not found_last_word:
                    found_last_word = True
                res += 1
            elif found_last_word:
                # If a space is found and we have found the last word, break the loop
                break
        return res