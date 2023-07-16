class Solution {
    public boolean judgeSquareSum(int c) {
        int left = 0;
        // Initialize the right pointer to the square root of c
        int right = (int) Math.sqrt(c); 
        // Continue looping until left becomes greater than right
        while (left <= right) { 
            // Calculate the sum of squares of left and right
            // Use long data type for sum calculation
            long sum = (long) left * left + (long) right * right; 
            if (sum == c) { 
                return true;
            } else if (sum < c) {
                // Increment the left pointer to consider a larger value
                left++; 
            } else {
                right--;
            }
        }

        return false;     
    }
}