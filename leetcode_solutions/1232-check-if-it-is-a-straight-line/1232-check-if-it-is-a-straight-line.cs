public class Solution {
    public bool CheckStraightLine(int[][] coordinates) {
       if (coordinates.Length <= 2)
        {
            return true;
        }
        
        int[] point1 = coordinates[0];
        int[] point2 = coordinates[1];
        
        int dx = point2[0] - point1[0];
        int dy = point2[1] - point1[1];
        
        for (int i = 2; i < coordinates.Length; i++)
        {
            int[] point = coordinates[i];
            
            int dx1 = point[0] - point1[0];
            int dy1 = point[1] - point1[1];
            
            if (dx * dy1 != dy * dx1)
            {
                return false;
            }
        }
        
        return true;
        
    }
}