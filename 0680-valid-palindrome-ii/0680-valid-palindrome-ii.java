class Solution {
    public boolean validPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        while(left <= right){
            if(s.charAt(left) != s.charAt(right)){
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
    
    // Helper method that only deals with alpha numeric values
    private boolean isAlphaNumeric(char c){
        return ('A' <= c && c <= 'Z') ||
               ('a' <= c && c <= 'z') ||
               ('0' <= c && c <= '9');
    }
}