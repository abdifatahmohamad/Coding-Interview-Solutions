class Solution {
    public int maxArea(int[] heights) {
        int left = 0;
        int right = heights.length - 1;
        int maxArea = Integer.MIN_VALUE;
        while(left < right){
            // The formula of area is width * height
            // Calculate width
            int width = right - left;
            // Calculate height
            int height = Math.min(heights[left], heights[right]);
            // Calculate area
            int area = width * height;
            // Calculate max are 
            maxArea = Math.max(maxArea, area);
            
            // Update pointers
            if(heights[left] < heights[right]){
                left++;
            }else if(heights[left] > heights[right]){
                right--;
            }else{
            // If both heiht[left] and height[right] are equal, 
            // move either pointer (doesn't matter)
                left++;
            }
            
        }
        
        return maxArea;
    }
}