public class Solution {
    public int CountNegatives(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;

        int i = m - 1, j = 0;

        int res = 0;
        while(i >= 0 && j < n){
            // If we found a negative number, move up a row
            if(grid[i][j] < 0){
                res += n - j;
                i--;
            // Else, move right to see if we can find the negative number
            } else{
                j++;
            }
        }
        
        return res;
        
    }
}