class Solution {
    public int[] shortestToChar(String s, char c) {
        char[] chars = s.toCharArray();
        int[] res = new int[s.length()];
        // Find the closest occurrence of c for each index 0
        int left = -1;
        int right = -1;
        int i = 0;
        while (i < chars.length) {
            if (chars[i] == c) {
                // Update the left pointer if the current character is the target
                left = i; 
            }

            if (left != -1) {
                // Calculate the distance to the left pointer if it has been set
                res[i] = i - left; 
            }

            i++;
        }
        
        // Reset the loop counter to the last index
        i = chars.length - 1; 

        while (i >= 0) {
            if (chars[i] == c) {
                // Update the right pointer if the current character is the target
                right = i; 
            }

            if (right != -1) {
                if (res[i] == 0) {
                    // Calculate the distance to the right pointer 
                    // if it has been set and no distance has been calculated yet
                    res[i] = right - i; 
                } else {
                    // Update the distance to the right pointer 
                    // if it is smaller than the current distance
                    res[i] = Math.min(res[i], right - i); 
                }
            }

            i--;
        }
        
        return res;
    }
}

