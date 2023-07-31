class Solution {
    public int[] leftRightDifference(int[] nums) {
        // if(nums.length == 1){
        //     return new int[]{0};
        // }

        int[] res = new int[nums.length];
        int[] leftSum = leftSum(nums);
        int[] rightSum = rightSum(nums);
        
        int n = leftSum.length;
        for (int i = 0; i < n; i++) {
            res[i] = Math.abs(leftSum[i] - rightSum[i]);
        }
        return res;
        
    }
    
    private int[] leftSum(int[] nums) {
        int n = nums.length;
        int[] leftSum = new int[n];
        int sum = 0;
        for (int i = 0; i < n; i++) {
            leftSum[i] = sum;
            sum += nums[i];
        }
        return leftSum;
    }
    
    private int[] rightSum(int[] nums) {
        int n = nums.length;
        int[] rightSum = new int[n];
        int sum = 0;
        for (int i = n - 1; i >= 0; i--) {
            rightSum[i] = sum;
            sum += nums[i];
        }
        return rightSum;
    }
}