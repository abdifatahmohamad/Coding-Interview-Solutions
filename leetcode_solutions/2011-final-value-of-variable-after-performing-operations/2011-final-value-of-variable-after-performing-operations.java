class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int x = 0;
        for(String s : operations){
            // if (s.equals("X++") || s.equals("++X")) {
            //     x++;
            // } else{
            //     x--;
            // }
            
            // Shorter version using ternary operator
            x += (s.equals("X++") || s.equals("++X")) ? 1 : -1;
        }
        return x;  
    }
}
