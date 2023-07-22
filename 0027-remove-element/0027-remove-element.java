class Solution {
    public int removeElement(int[] nums, int val) {
        int left = 0;
        int right = 1;
        while(right < nums.length){
            if(nums[left] != val){
                left++;
                right++;
            } else if(nums[right] == val){
                right++;
            }else{
                swab(nums, left, right);
            }       
        }
        
        int res = 0;
        for(int n : nums){
            if(n != val){
                res++;
            }
        }
        
        return res;
    }
    
    // Helper method that swabs two values
    private void swab(int[] nums, int left, int right){
        int temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;
    }
}