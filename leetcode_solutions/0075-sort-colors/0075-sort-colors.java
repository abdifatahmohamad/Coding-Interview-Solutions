class Solution {
    public void sortColors(int[] nums) {
        // Step 1: Create three buckets to represent the three colors.
        int[] buckets = new int[3];
        
        // Step 2: Traverse the input array 
        // and count the occurrences of each color.
        for (int n : nums) {
            buckets[n]++;
        }
        
        int index = 0;
        // Step 3: Modify the input array in-place.
        for (int color = 0; color < 3; color++) {
            while (buckets[color] > 0) {
                nums[index++] = color;
                buckets[color]--;
            }
        }
        
    }
}