class Solution {
    public String largestGoodInteger(String num) {
        String largestGood = ""; // Variable to store the largest good integer
        
        // Iterate through each possible 3-digit substring in the given string
        for (int i = 0; i <= num.length() - 3; i++) {
            String substring = num.substring(i, i + 3); // Extract the 3-digit substring
            
            // Check if the substring consists of only one unique digit
            if (isGoodInteger(substring)) {
                // Compare the current good integer with the largest one found so far
                if (substring.compareTo(largestGood) > 0) {
                    largestGood = substring; // Update the largest good integer
                }
            }
        }
        
        return largestGood;
    }
    
    
    // Helper method to check if a string is a good integer
    private boolean isGoodInteger(String str) {
        char firstChar = str.charAt(0);
        
        // Check if all characters in the string are equal to the first character
        for (int i = 1; i < str.length(); i++) {
            if (str.charAt(i) != firstChar) {
                return false;
            }
        }
        
        return true;
    }
}