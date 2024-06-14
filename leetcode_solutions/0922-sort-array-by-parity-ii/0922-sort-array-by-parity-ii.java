class Solution {
    public int[] sortArrayByParityII(int[] nums) {
        int n = nums.length;
        int odd = 1;
        int even = 0;
        // Iterate until both odd and even indices are within the array bounds
        while (odd < n && even < n) { 
            // If the element at the odd index is even 
            // and the element at the even index is odd
            if (nums[odd] % 2 < nums[even] % 2) { 
                // Swap the elements at the odd and even indices
                swap(nums, odd, even); 
            }
            // If the element at the odd index is odd
            if (nums[odd] % 2 == 1) { 
                // Move to the next odd index
                odd += 2; 
            }
            // If the element at the even index is even
            if (nums[even] % 2 == 0) { 
                // Move to the next even index
                even += 2; 
            }
        }
        return nums;
    }
    
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i]; // Store the value at index i in a temporary variable
        nums[i] = nums[j]; // Replace the value at index i with the value at index j
        nums[j] = temp; // Replace the value at index j with the temporary value
    }
    
    
    // Without helper method
    public int[] sortArrayByParityIIHelperMethod(int[] nums) {
        int n = nums.length;
        int odd = 1;
        int even = 0;
        while(odd < n && even < n){
            if (nums[odd] % 2 < nums[even] % 2){
                int temp = nums[odd];
                nums[odd] = nums[even];
                nums[even] = temp;
            }
            if (nums[odd] % 2 == 1)
                odd += 2;
            if (nums[even] % 2 == 0)
                even += 2;
        }
        return nums;
    }
}

/*
[4, 2, 5, 7] indices [0, 1, 2, 3]
[0, 1, 2, 3]



*/