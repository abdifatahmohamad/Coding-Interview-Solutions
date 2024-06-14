class Solution {
    public int countElements(int[] nums) {
        
        // Find the minimum and maximum elements in the array
        int minVal = Integer.MAX_VALUE;
        int maxVal = Integer.MIN_VALUE;
        for (int n : nums) {
            minVal = Math.min(minVal, n);
            maxVal = Math.max(maxVal, n);
        }
        
        System.out.println(minVal);
        System.out.println(maxVal);

        int res = 0;

        // Count elements with both strictly smaller and strictly greater elements
        for (int n : nums) {
            // Check if the element has both strictly smaller and strictly greater elements
            if (n > minVal && n < maxVal)  
                res++;
        }

        return res;  // Return the final count
    }
}
