class Solution {
    public int maximumValue(String[] strs) {
        int maxVal = Integer.MIN_VALUE;
        for(String s : strs){
            int value = getValue(s);
            // System.out.println(value);
            maxVal = Math.max(maxVal, value);
        }
        
        return maxVal;
        
    }
    
    private int getValue(String s){
        int value = 0;
        int placeValue = 1;
        for(int i = s.length() -1; i >= 0; i--){
            char c = s.charAt(i);
            if(!Character.isDigit(c)){
                return s.length();
            }
            int digit = c - '0';
            value += (digit * placeValue);
            placeValue *= 10;
        }
        
        
        return value;
    }
}