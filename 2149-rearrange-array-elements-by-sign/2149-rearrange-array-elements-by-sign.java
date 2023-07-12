class Solution {
    public int[] rearrangeArray(int[] nums) {
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

        int[] res = new int[n];
        int idx = 0;
        for (int i = 0; i < n / 2; i++) {
            res[idx++] = pos[i];
            res[idx++] = neg[i];
        }

        // If there are any remaining elements in either positive or negative array, add them to the result
        if (posIndex < n / 2) {
            res[idx++] = pos[idx];
        }

        if (negIndex < n / 2) {
            res[idx++] = neg[idx];
        }

    return res;
        
    }
}