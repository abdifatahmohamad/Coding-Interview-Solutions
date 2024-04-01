class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for i in range(len(s)-1,-1,-1):
            # If the current character is a space and length is non-zero
            if s[i] == " " and length:
                # If the current character is a space and we've already encountered characters of the last word,
                # return the length (indicating the end of the last word)
                return length
            # If the current character is not a space, increment the length
            elif s[i] != " ":
                length += 1
        # If the loop completes without finding any spaces, return the calculated length
        return length
