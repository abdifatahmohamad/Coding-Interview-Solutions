class Solution {
    public boolean isPrefixString(String s, String[] words) {
           StringBuilder sb = new StringBuilder();

        for (int i = 0; i < words.length; i++) {
            sb.append(words[i]);
            if (sb.length() >= s.length()) {
                break;
            }
        }

        return sb.toString().equals(s);
    }
}