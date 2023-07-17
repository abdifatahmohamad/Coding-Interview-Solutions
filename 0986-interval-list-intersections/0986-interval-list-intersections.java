class Solution {
    // https://www.youtube.com/watch?v=l3lWrfGiAFI
    public int[][] intervalIntersection(int[][] nums1, int[][] nums2) {
        // Result list
        List<int[]> res = new ArrayList<>();
        // Get the length of both list
        int n1 = nums1.length, n2 = nums2.length;
        // Define pointers
        int i = 0, j = 0; // i for nums1 pointer, j for nums2 pointer
        
        // Find intervals
        while(i < n1 && j < n2){
            // Define start time and end time for both list
            int s1 = nums1[i][0]; // nums1 start time
            int e1 = nums1[i][1]; // nums1 end time
            int s2 = nums2[j][0]; // nums2 start time
            int e2 = nums2[j][1]; // nums2 end time
            // If there is an intersection
            if((s1 <= s2 && s2 <= e1) || (s2 <= s1 && s1 <= e2)){
                // Find start and en time intervals for the result list
                int start = Math.max(s1, s2);
                int end = Math.min(e1, e2);
                // Puth start and end in a temp list
                int[] temp = {start, end};
                // Add that temp list to the result list
                res.add(temp);
            }
            
            // Move pointers
            if(e2 > e1){
                // Move nums1 i pointer to the right
                i++;
            }else{
                // Move nums2 j pointer to the right
                j++;
            }
        }
        
        // Return the result in 2D array, for each interval we gonna have
        // two slots; start time and end time
        return res.toArray(new int[res.size()][]);
        
    }
}
