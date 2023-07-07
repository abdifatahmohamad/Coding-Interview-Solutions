class Solution {
    public boolean backspaceCompare(String s, String t) {   
        return processString(s).equals(processString(t));       
    }
    
    private String processString(String str) {
        StringBuilder sb = new StringBuilder();
        for (char c : str.toCharArray()) {
            if (c == '#') {
                // If the current character is '#', 
                // remove the last character from the string builder (if it exists)
                if (sb.length() > 0) {
                    sb.deleteCharAt(sb.length() - 1);
                }
                
            } else {
                // If the current character is not '#', append it to the string builder
                sb.append(c);
            }
        }
        return sb.toString();
    }
}