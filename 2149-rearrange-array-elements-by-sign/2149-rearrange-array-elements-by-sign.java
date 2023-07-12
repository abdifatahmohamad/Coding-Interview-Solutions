class Solution {
    public int[] rearrangeArray(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        int i = 0; // positive index
        int j = 1; // negative index

        // Separate positive and negative numbers into separate arrays 
        // while populating the result array
        for (int num : nums) {
            if (num < 0) {
                res[j] = num;
                j += 2;
            } else {
                res[i] = num;
                i += 2;
            }
        }

        return res;
    }
    
    // 
    public int[] rearrangeArrayMine(int[] nums) {
        int n = nums.length;
        int[] pos = new int[n / 2];
        int[] neg = new int[n / 2];
        
        int posIndex = 0;
        int negIndex = 0;

        // Separate positive and negative numbers into separate arrays
        for (int i = 0; i < n; i++) {
            if (nums[i] < 0) {
                neg[negIndex++] = nums[i];
            } else {
                pos[posIndex++] = nums[i];
            }
        }
        int idx = 0;
        for (int i = 0; i < n / 2; i++) {
            nums[idx++] = pos[i];
            nums[idx++] = neg[i];
        }

        // If there are any remaining elements in either positive or negative array, add them to the result
        if (posIndex < n / 2) {
            nums[idx++] = pos[idx];
        }

        if (negIndex < n / 2) {
            nums[idx++] = neg[idx];
        }

    return nums;
        
    }
}