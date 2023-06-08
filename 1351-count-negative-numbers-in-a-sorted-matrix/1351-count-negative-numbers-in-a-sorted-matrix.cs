public class Solution {
    public int CountNegatives(int[][] grid) {
        int rows = grid.Length;
        int cols = grid[0].Length;
        int res = 0;
        
        for(int r = 0; r < rows; r++){
            for(int c = 0; c < cols; c++){
                int value = grid[r][c];
                if(value < 0){
                    res++;
                }
                
            }
        }
        
        return res;
        
    }
}