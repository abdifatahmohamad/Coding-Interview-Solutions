class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # get the number of rows and columns in the grid
        rows, cols = len(grid), len(grid[0])

        # create a 2D array to store the minimum path sum up to each cell
        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        # initialize the minimum path sum for the bottom-right corner cell
        dp[rows - 1][cols - 1] = grid[rows - 1][cols - 1]

        # initialize the minimum path sum for the last row
        for j in range(cols - 2, -1, -1):
            dp[rows - 1][j] = dp[rows - 1][j + 1] + grid[rows - 1][j]

        # initialize the minimum path sum for the last column
        for i in range(rows - 2, -1, -1):
            dp[i][cols - 1] = dp[i + 1][cols - 1] + grid[i][cols - 1]

        # compute the minimum path sum for the rest of the cells
        for i in range(rows - 2, -1, -1):
            for j in range(cols - 2, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])

        # return the minimum path sum at the top-left corner of the grid
        return dp[0][0]
        