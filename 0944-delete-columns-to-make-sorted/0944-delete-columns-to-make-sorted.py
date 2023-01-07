class Solution:
    def minDeletionSize(self, s: List[str]) -> int:
        rows, cols = len(s) - 1, len(s[0])
        min_deletions = 0
        for i in range(cols):
            for j in range(rows):
                if s[j][i] > s[j + 1][i]:
                    min_deletions += 1
                    break
                    
        return min_deletions
        