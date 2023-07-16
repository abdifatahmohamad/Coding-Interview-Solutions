class Solution {
    public boolean judgeSquareSum(int c) {
         // Calculate the square root of c
        int cSqr = (int) Math.sqrt(c);
        // Create an array to store numbers from 0 to cSqr
        int[] nums = new int[cSqr + 1];
        // Fill the nums array with numbers from 0 to cSqr
        for (int i = 0; i <= cSqr; i++) {
            nums[i] = i;
        }

        int left = 0;
        int right = cSqr;
        while (left <= right) {
            // Calculate the sum of squares
            long sum = (long) nums[left] * nums[left] + (long) nums[right] * nums[right];
            
            // Check if the sum is equal to c
            if (sum == c) {
                return true; // Two numbers found whose squares sum up to c
            } else if (sum < c) {
                left++; // Increment the left pointer to consider a larger number
            } else {
                right--; // Decrement the right pointer to consider a smaller number
            }
        }

        return false;     
    }
}