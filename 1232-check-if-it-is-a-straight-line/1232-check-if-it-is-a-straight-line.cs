public class Solution {
    public bool CheckStraightLine(int[][] coordinates) {
        if (coordinates.Length == 2)
        {
            return true;
        }
        
        int[] point1 = coordinates[0];
        int[] point2 = coordinates[1];
        
        for (int i = 2; i < coordinates.Length; i++)
        {
            int[] point = coordinates[i];
            
            // Calculate cross product
            int crossProduct = (point2[0] - point1[0]) * (point[1] - point1[1]) -
                               (point2[1] - point1[1]) * (point[0] - point1[0]);
            
            if (crossProduct != 0)
            {
                return false;
            }
        }
        
        return true;
        
    }
}