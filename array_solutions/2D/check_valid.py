import collections


def checkValid(matrix) -> bool:
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

    '''
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
    '''
    # n = len(matrix)
    # for i in range(n):
    #     rowsSet = set()
    #     for j in range(n):
    #         value = matrix[i][j]
    #         rowsSet.add(value)
    #     if len(rowsSet) != n:
    #         return False
    #
    # for i in range(n):
    #     colsSet = set()
    #     for j in range(n):
    #         value = matrix[j][i]
    #         colsSet.add(value)
    #     if len(colsSet) != n:
    #         return False
    # return True


print(checkValid([
    [1, 2, 3],
    [3, 1, 2],
    [2, 3, 1]
]))

print(checkValid([
    [1, 1, 1],
    [1, 2, 3],
    [1, 2, 3]
]))
