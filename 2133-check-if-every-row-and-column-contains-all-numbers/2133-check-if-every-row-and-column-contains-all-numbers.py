class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(n):
            rowsSet = set()
            for j in range(n):
                value = matrix[i][j]
                rowsSet.add(value)
            if len(rowsSet) != n:
                return False

        for i in range(n):
            colsSet = set()
            for j in range(n):
                value = matrix[j][i]
                colsSet.add(value)
            if len(colsSet) != n:
                return False
        return True
        