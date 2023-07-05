class Solution {
    public int longestSubarray(int[] nums) {
        int left = 0; // left pointer of the sliding window
        int right = 0; // right pointer of the sliding window
        int zeros = 0; // number of zeros in the current window
        int maxLength = 0; // length of the longest subarray

        while (right < nums.length) {
            if (nums[right] == 0) {
                zeros++; // increment zeros count
            }

            while (zeros > 1) {
                if (nums[left] == 0) {
                    zeros--; // decrement zeros count
                }
                left++; // move left pointer to the right
            }

            maxLength = Math.max(maxLength, right - left); // update maxLength

            right++; // move right pointer to the right
        }

        return maxLength;
    }
}