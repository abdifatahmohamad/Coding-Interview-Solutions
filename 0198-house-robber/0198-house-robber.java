class Solution {
    public int rob(int[] nums) {
        int n = nums.length;

        if (n == 1) {
            return nums[0];
        }

        // Create an array to store the maximum money that can be collected until each index
        int[] dp = new int[n];

        // Base case: the first element can be collected
        dp[0] = nums[0];

        // Second element can be collected if it's greater than the first element
        dp[1] = Math.max(nums[0], nums[1]);

        // Calculate maximum money for each index starting from the third element
        for (int i = 2; i < n; i++) {
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
        }

        return dp[n - 1];
        
    }
}