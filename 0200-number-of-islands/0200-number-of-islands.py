class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != "1" or (r, c) in visited:
                return 0
            visited.add((r, c))
            for x, y in [(0,1),(1,0),(0,-1),(-1,0)]:
                dr, dc = r + x, c + y
                dfs(dr, dc)
            return 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] not in visited and grid[r][c] == "1": 
                    islands += dfs(r, c)
        
        return islands
                    