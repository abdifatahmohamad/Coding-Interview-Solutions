class Solution {
    public String largestOddNumber(String num) {
        int n = num.length();
        
        // Iterate from the rightmost digit of the string
        for (int i = n - 1; i >= 0; i--) {
            int digit = num.charAt(i) - '0';
            
            // Check if the digit is odd
            if (digit % 2 == 1) {
                return num.substring(0, i + 1); // Return the substring from the start to the current index
            }
        }
        
        return ""; // Return an empty string if no odd number is found
    }
}