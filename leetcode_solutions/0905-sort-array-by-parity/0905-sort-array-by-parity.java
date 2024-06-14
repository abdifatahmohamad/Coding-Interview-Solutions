class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        
        while (left < right) {
            // Move left pointer until an odd number is found
            while (nums[left] % 2 == 0 && left < right) {
                left++;
            }
            
            // Move right pointer until an even number is found
            while (nums[right] % 2 == 1 && left < right) {
                right--;
            }
            
            // Swap the odd number on the left with the even number on the right
            if (left <= right) {
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
            }
        }
        return nums;
    }
}