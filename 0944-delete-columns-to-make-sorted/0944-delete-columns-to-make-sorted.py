class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if strs is None or len(strs) == 0:
            return 0

        deletions = 0
        for col in range(len(strs[0])):
            char = strs[0][col]
            for word in range(len(strs)):
                if strs[word][col] < char:
                    deletions += 1
                    break
                char = strs[word][col]

        return deletions
        