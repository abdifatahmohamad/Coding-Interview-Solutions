from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Get the initial color of the starting pixel
        iniColor = image[sr][sc]
        
        # If the initial color is the same as the target color, return the original image
        if iniColor == color:
            return image

        # Get the number of rows and columns in the image
        rows, cols = len(image), len(image[0])
        
        # Create a new matrix (res) and copy the values from the original image
        res = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                res[i][j] = image[i][j]

        # Create a visited matrix to keep track of visited pixels
        visited = set()
        
        # Define the DFS helper function
        def dfs(r, c):
            # Mark the current pixel as visited
            visited.add((r, c))
            # Change the color of the current pixel in the result matrix
            res[r][c] = color
            # Direction vectors for moving right, left, up, and down
            left, right, top, down = (0, -1), (0, 1), (-1, 0), (1, 0)
            # Iterate over all four directions
            for x, y in [right, left, top, down]:
                dr, dc = r + x, c + y
                # Check if the new position is within bounds, not visited, and has the initial color
                # if 0 <= dr < rows and 0 <= dc < cols and (dr, dc) not in visited and image[dr][dc] == iniColor:
                #     # Recursively apply DFS to the neighboring pixel
                #     dfs(dr, dc)
                
                # Check if the new position is within bounds, not visited, and has the initial color
                if dr < 0 or dc < 0 or dr == rows or dc == cols or \
                    (dr, dc) in visited or image[dr][dc] != iniColor:
                    continue
                # Recursively apply DFS to the neighboring pixel
                dfs(dr, dc)
        
        # Start the DFS from the initial pixel
        dfs(sr, sc)
        # Return the result matrix
        return res

# Example usage:
image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
sr, sc, color = 1, 1, 2
solution = Solution()
result = solution.floodFill(image, sr, sc, color)
for row in result:
    print(row)