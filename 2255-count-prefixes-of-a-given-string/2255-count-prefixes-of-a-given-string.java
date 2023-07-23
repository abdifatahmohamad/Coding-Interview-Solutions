class Solution {
    public int countPrefixes(String[] words, String s) {
        int res = 0;
        for (int i = 0; i < words.length; i++) {
            if (s.startsWith(words[i])) {
                res++;
            }
        }
        
        return res;    
    } 
    
    // Helper method that checks if string starts with
    private boolean startsWith(String word, String prefix) {
        if (word.length() < prefix.length()) {
            return false;
        }

        for (int i = 0; i < prefix.length(); i++) {
            if (word.charAt(i) != prefix.charAt(i)) {
                return false;
            }
        }

        return true;
    }
}