class Solution {
    public int minSwaps(String s) {
        int extraClosing = 0;
        int res = Integer.MIN_VALUE;
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '['){
                extraClosing--;          
            }else{
                extraClosing++;
            }
            
            res = Math.max(res, extraClosing);
        } 
        return (res + 1) / 2;      
    }
}


/*
  s = "]]][[["
  i =  012345
  s = "[[][]]"

*/