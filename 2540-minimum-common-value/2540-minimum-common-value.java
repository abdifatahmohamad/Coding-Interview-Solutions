class Solution {
    public int getCommon(int[] nums1, int[] nums2) {
        int smallest = Integer.MAX_VALUE;
        int i = 0;
        int j = 0;
        // Iterate while both pointers are within array bounds
        while (i < nums1.length && j < nums2.length) {
            // Case1: if values at the pointers are equal
            if (nums1[i] == nums2[j]) {
                // Update smallest if necessary
                smallest = Math.min(smallest, nums1[i]); 
                i++; 
                j++;
            // Case2: if value at i pointer is smaller
            } else if (nums1[i] < nums2[j]) { 
                i++;
            } else { // Case3: if value at j pointer is smaller
                j++;
            }
        }
        // Return smallest if it has been updated, otherwise return -1
        return (smallest != Integer.MAX_VALUE) ? smallest : -1; 
    }
}