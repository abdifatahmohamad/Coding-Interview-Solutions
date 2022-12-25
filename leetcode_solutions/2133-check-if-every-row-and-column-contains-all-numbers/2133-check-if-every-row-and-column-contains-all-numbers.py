class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rowsSet = collections.defaultdict(set)
        colsSet = collections.defaultdict(set)
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                value = matrix[r][c]
                if value in rowsSet[r] or value in colsSet[c]:
                    return False
                rowsSet[r].add(value)
                colsSet[c].add(value)
        return True
        