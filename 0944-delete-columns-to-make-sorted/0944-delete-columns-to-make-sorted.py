class Solution:
    def minDeletionSize(self, s: List[str]) -> int:
        rows, cols = len(s) - 1, len(s[0])
        min_deletions = 0
        for i in range(cols):  # Iterate through the characters in each string
            for j in range(rows):  # Compare each character to the character in the same position in the next string
                if s[j][i] > s[j + 1][i]:  # If the character in the later string is lexicographically smaller
                    min_deletions += 1  # Increment min_deletions
                    break  # Continue to the next character
        return min_deletions
        