class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> window = new HashSet<>();
        
        int left = 0;
        for (int right = 0; right < nums.length; right++) {
            
            // Check if window too large
            if (right - left > k) {
                // remove the leftmost value
                window.remove(nums[left]);
                // increment the left pointer
                left++;
            }
            
            // Valid window
            if (window.contains(nums[right])) {
                return true;
            } else {
                // add the value to the window
                window.add(nums[right]);
            }
        }
        
        return false;
        
    }
        
}
