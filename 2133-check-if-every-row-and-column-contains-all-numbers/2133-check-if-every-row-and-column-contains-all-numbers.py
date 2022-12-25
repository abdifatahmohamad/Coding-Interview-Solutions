class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rowsSet = collections.defaultdict(set)
        colsSet = collections.defaultdict(set)
        n = len(matrix)
        for r in range(n):
            for c in range(n):
                if matrix[r][c] in rowsSet[r] or matrix[r][c] in colsSet[c]:
                    return False
                rowsSet[r].add(matrix[r][c])
                colsSet[c].add(matrix[r][c])
        return True
        