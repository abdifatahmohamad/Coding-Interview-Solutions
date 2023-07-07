class Solution {
    public boolean backspaceCompare(String s, String t) {
        return processString(s).equals(processString(t));
    }
    
    // Helper method that removes string #
    private String processString(String s){
        StringBuilder sb = new StringBuilder();
        for(char ch : s.toCharArray()){
            if(ch == '#'){
                if(sb.length() > 0){
                    sb.deleteCharAt(sb.length() - 1);
                }
            } else{
                sb.append(ch);
            }
        }
        
        return sb.toString();
    }
    
    
}