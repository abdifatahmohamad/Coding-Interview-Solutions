class Solution {
    public boolean isPrefixString(String s, String[] words) {
        StringBuilder sb = new StringBuilder();
        int i = 0;
        // Keep adding words array to the sb until
        // sb length < given input string s
        while (i < words.length && sb.length() < s.length()) {
            // keep concatinating words
            sb.append(words[i]);
            i++;
        }

        return sb.toString().equals(s);
    }
}