class Solution {
    public boolean validPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        while(left <= right){
            // If the characters at left and right are not equal
            if(s.charAt(left) != s.charAt(right)){
                // Try skipping the character at left and 
                // check if the remaining substring is a palindrome
                
                // Try skipping the character at right and 
                // check if the remaining substring is a palindrome
                if(isPalindrome(s, left + 1, right) || isPalindrome(s, left, right - 1)){
                    return true;
                } else{
                    return false;
                }
            }
            
            left++;
            right--;
        }
        
        return true;
    }
    
    // Helper method that validates if string is palindrome or not
    private boolean isPalindrome(String s, int left, int right){
        while(left <= right){
            if(s.charAt(left) != s.charAt(right)){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}