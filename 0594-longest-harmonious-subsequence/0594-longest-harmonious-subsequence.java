class Solution {
    public int findLHS(int[] nums) {
        // https://www.youtube.com/watch?v=tgkpqp5-6Os
        Arrays.sort(nums);
        int left = 0;
        int right = 1;
        int longest = Integer.MIN_VALUE;
        while(right < nums.length){
            int diff = nums[right] - nums[left];
            if(diff == 1){
                int window = (right - left) + 1;
                longest = Math.max(longest, window);
            }
            // 2 2 3
            if(diff<= 1){
                right++;
            }else{
                // shrink the window
                left++;
            }
        }
        
        return Integer.MIN_VALUE != longest ? longest : 0;
        
    }
}