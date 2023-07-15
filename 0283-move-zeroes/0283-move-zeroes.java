class Solution {
    public void moveZeroes(int[] nums) {
        // Base case
        if(nums.length < 2){
            return;
        }
        int left = 0;
        int right = 1;
        while(right < nums.length){
            if(nums[left] != 0){
                left++;
                right++;
            } else if(nums[right] == 0){
                right++;
            }else{
                swab(nums, left, right);
            }       
        }     
    }
    
    // Helper method that swabs two values
    private void swab(int[] nums, int left, int right){
        int temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;
    }
}