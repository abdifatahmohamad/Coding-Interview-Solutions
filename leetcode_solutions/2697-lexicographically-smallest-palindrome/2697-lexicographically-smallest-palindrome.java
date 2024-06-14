class Solution {
    public String makeSmallestPalindrome(String s) {
        if (s == null || s.length() < 2) {
            return s; 
        }

        int left = 0;
        int right = s.length() - 1;

        // Use a StringBuilder for modifying the string
        StringBuilder sb = new StringBuilder(s); 

        while (left < right) {
            if (sb.charAt(left) == sb.charAt(right)) {
                left++;
                right--;
            } else {
                if (sb.charAt(left) > sb.charAt(right)) {
                    // Replace character at left with character at right
                    sb.setCharAt(left, sb.charAt(right)); 
                } else {
                     // Replace character at right with character at lef
                    sb.setCharAt(right, sb.charAt(left));
                }
                left++;
                right--;
            }
        }

        return sb.toString(); // Return the modified string
        
    }
}