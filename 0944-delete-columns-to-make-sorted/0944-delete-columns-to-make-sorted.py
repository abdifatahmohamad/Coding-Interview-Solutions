class Solution:
    def minDeletionSize(self, s: List[str]) -> int:
        min_deletions = 0
        for i in range(len(s[0])):
            for j in range(len(s) - 1):
                if s[j][i] > s[j + 1][i]:
                    min_deletions += 1
                    break
                    
        return min_deletions
        