class Solution {
    public int minSwaps(String s) {
        Stack<Character> stack = new Stack<>();
        int swabs = 0;
        for(char ch : s.toCharArray()){
            if(ch == '['){
                stack.add(ch);
            } else{
                if(!stack.isEmpty() && ch == ']'){
                    stack.pop();
                }else{
                    swabs++;
                }
            }
        }
        
        return (swabs + 1) / 2;
    }
}