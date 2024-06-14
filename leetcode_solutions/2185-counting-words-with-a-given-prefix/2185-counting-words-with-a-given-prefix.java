class Solution {
    public int prefixCount(String[] words, String pref) {
        int res = 0;
        for (int i = 0; i < words.length; i++) {
            if (words[i].startsWith(pref)) {
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