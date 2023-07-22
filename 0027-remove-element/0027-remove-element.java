class Solution {
    public int removeElement(int[] nums, int val) {
        int left = 0;
        int right = 0;
        int k = 0;
        while(right < nums.length){
            if(nums[right] != val){
                nums[k] = nums[right];
                left++;
                k++;
            }
            
            right++;
        }
        return k;    
    }
}