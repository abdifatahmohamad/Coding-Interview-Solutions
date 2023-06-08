public class Solution {
    public int CountNegatives(int[][] matrix) {
        int rows = matrix.Length;
        int cols = matrix[0].Length;

        bool[,] visited = new bool[rows, cols];
        int count = 0;

        int[] dr = { -1, 1, 0, 0 };
        int[] dc = { 0, 0, -1, 1 };

        Queue<int[]> queue = new Queue<int[]>();

        queue.Enqueue(new int[] { 0, 0 });  // Start from the top-left corner

        while (queue.Count > 0)
        {
            int[] currPos = queue.Dequeue();
            int r = currPos[0];
            int c = currPos[1];

            // Check if the current position is within the matrix boundaries
            if (r >= 0 && r < rows && c >= 0 && c < cols && !visited[r, c])
            {
                visited[r, c] = true;

                // Check if the current value is negative
                if (matrix[r][c] < 0)
                {
                    count++;
                }

                // Enqueue the adjacent positions
                for (int i = 0; i < 4; i++)
                {
                    int newRow = r + dr[i];
                    int newCol = c + dc[i];
                    queue.Enqueue(new int[] { newRow, newCol });
                }
            }
        }

        return count;
        
    }
}