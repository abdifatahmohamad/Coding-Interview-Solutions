class Solution {
    public int removeElement(int[] nums, int val) {
        int left = 0;
        int right = 0;
        int res = 0;
        while(right < nums.length){
            if(nums[right] != val){
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                left++;
                res++;
            }
            
            right++;
        }
        return res;    
    }
}