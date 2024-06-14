class Solution {
    public int countPairs(List<Integer> nums, int target) {
        int count = 0;
        int n = nums.size();

        // Sort the array in non-decreasing order
        Collections.sort(nums);

        // Use two pointers approach
        int left = 0;
        int right = n - 1;

        while (left < right) {
            int sum = nums.get(left) + nums.get(right);

            // If the sum is less than the target, then all pairs with the current left pointer
            // and any pointer between left and right will satisfy the condition
            if (sum < target) {
                count += (right - left);
                left++;
            } else {
                // If the sum is greater than or equal to the target, move the right pointer to the left
                right--;
            }
        }

        return count;
    }
}