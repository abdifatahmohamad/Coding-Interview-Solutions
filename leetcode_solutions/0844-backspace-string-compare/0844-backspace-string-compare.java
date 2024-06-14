class Solution {
    public boolean backspaceCompare(String s, String t) {
        return processString(s).equals(processString(t));
    }
    
    // Helper method that removes string #
    private String processString(String s) {
        // Create a stack to store characters
        Stack<Character> stack = new Stack<>();
        
        // Iterate over each character in the string
        for (char ch : s.toCharArray()) {
            if (ch == '#') {
                // Handle backspace: if stack is not empty, remove the topmost character
                if (!stack.isEmpty()) {
                    stack.pop();
                }
            } else {
                // Add non-backspace character to the stack
                stack.push(ch);
            }
        }
        
        // Build the final string from the characters in the stack
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.insert(0, stack.pop());
        }
        
        // Return the processed string
        return sb.toString();
    }
    
    
}