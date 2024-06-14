from typing import List

# Number of islands solution using DFS (Recursive Implementation)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r: int, c: int) -> None:
            visited.add((r, c))
            for x, y in [[1,0],[-1,0],[0,1],[0,-1]]:
                dr, dc = r + x, c + y 
                if dr < 0 or dr == rows or dc < 0 or dc == cols or \
                grid[dr][dc] != '1' or (dr,dc) in visited:
                    continue
                dfs(dr, dc)                

        for r in range(rows): 
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1
        
        return islands

# Number of islands solution using DFS (Iterative implementation) 
# DFS solution using iterative 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r: int, c: int) -> None:
            stack = [(r, c)]
            while stack: 
                r, c = stack.pop()
                if (r,c) in visited:
                    continue
                visited.add((r,c))
                for x, y in [[1,0],[-1,0],[0,1],[0,-1]]:
                    dr, dc = r + x, c + y
                    if dr < 0 or dr == rows or dc < 0 or dc == cols or \
		                grid[dr][dc] != '1' or (dr,dc) in visited:
                        continue
                    stack.append((dr, dc))
                
        for r in range(rows): 
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1
        
        return islands
    
# ======================================================
# Number of islands (BFS)
# BFS solution 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def bfs(r: int, c: int) -> None:
            queue = deque([(r, c)])
            visited.add((r, c))
            while queue: 
                r, c = queue.popleft()
                for direction in [[0,1],[1,0],[0,-1],[-1,0]]:
                    x, y = r + direction[0], c + direction[1]
                    if x < 0 or y < 0 or x == rows or y == cols \
                    or (x, y) in visited or grid[x][y] != '1':
                        continue 
                    visited.add((x, y))
                    queue.append((x, y))
                
        for r in range(rows): 
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == '1':
                    bfs(r, c)
                    islands += 1
        
        return islands


