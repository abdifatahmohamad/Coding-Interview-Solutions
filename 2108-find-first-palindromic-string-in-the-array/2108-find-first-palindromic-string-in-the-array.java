class Solution {
    public String firstPalindrome(String[] words) {
        for(String s : words){
            if(isPalindrome(s)){
                return s;
            }
        }
        
        return "";
        
    }
    
    private boolean isPalindrome(String s){
        int right = s.length() - 1;
        int left = 0;
        while(left < right){
            if(s.charAt(left) != s.charAt(right)){
                return false;
            }
            
            left ++;
            right--;
        }
        
        return true;
    }
    
    
}