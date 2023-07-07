class Solution {
    public String removeStars(String s) {
        return processString(s);
    }
    
    // Helper method that removes string #
    private String processString(String s){
        StringBuilder sb = new StringBuilder();
        for(char ch : s.toCharArray()){
            if(ch == '*'){
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