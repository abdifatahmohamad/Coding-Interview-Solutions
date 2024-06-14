class Solution {
    public int removeDuplicates(int[] nums) {
        int n = nums.length;
        int left = 0;
        int right = 1;
        while(right < n){
            if(nums[left] == nums[right]){
                right++;
            }else{
                // Remove duplicates
                left++;
                nums[left] = nums[right];
            }
        }
        
        return left + 1;
        
        
    }
}