class Solution {
    public void rotate(int[] nums, int k) {
        // Handle the edge case where k is greater than the length of the array
        if(k >= nums.length){
            k %= nums.length;
        }
        
        reverse(nums, 0, nums.length-1);  // reverse the whole array
        reverse(nums, 0, k-1);  // reverse the first part
        reverse(nums, k, nums.length-1);  // reverse the second part
        
        }

    public void reverse(int[] nums, int l, int r) {
        while (l < r) {
            int tmp = nums[l];
            nums[l++] = nums[r];
            nums[r--] = tmp;
        }
    }
        
}