class Solution:
    def minimumEffortPath(self, puzzle: List[List[int]]) -> int:
        rows, cols = len(puzzle), len(puzzle[0])
        # Initialize all puzzle/matrix to infinity values
        dist = [[float("Inf")] * cols for _ in range(rows)]
        # dist[0][0] = 0
        # Priority queue that represents a tuple which holds distance, row, and col
        pq = [(0, 0, 0)]
        # All four directions
        left, right, top, down = (0, -1), (0, 1), (-1, 0), (1, 0)

        while len(pq) > 0:
            effort, r, c = heappop(pq)
            if effort > dist[r][c]:
                continue  # this is an outdated version -> skip it
            # We reached the bottom right
            if r == rows - 1 and c == cols - 1:
                return effort

            for x, y in [right, left, top, down]:
                new_row, new_col = r + x, c + y
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    new_dist = max(effort, abs(puzzle[new_row][new_col] - puzzle[r][c]))
                    if dist[new_row][new_col] > new_dist:
                        dist[new_row][new_col] = new_dist
                        heappush(pq, (int(dist[new_row][new_col]), new_row, new_col))

        # Return 0 if we hit cell (m-1, n-1) and it's unreachable
        return 0