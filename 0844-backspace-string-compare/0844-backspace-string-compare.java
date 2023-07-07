class Solution {
    public boolean backspaceCompare(String s, String t) {   
        int i = s.length() - 1; // Initialize pointer i to the last character of string S
        int j = t.length() - 1; // Initialize pointer j to the last character of string T

        while (i >= 0 || j >= 0) { // Iterate until either pointer i or j reaches the beginning of their respective strings
            i = processString(s, i); // Process string S and update pointer i
            j = processString(t, j); // Process string T and update pointer j

            if (i >= 0 && j >= 0 && s.charAt(i) != t.charAt(j)) {
                // If both strings have non-skipped characters at the same index and they are not equal, return false
                return false;
            }

            if ((i >= 0) != (j >= 0)) {
                // If one string has more non-skipped characters than the other, return false
                return false;
            }

            i--; // Decrement pointer i
            j--; // Decrement pointer j
        }

        return true;       
    }
    
    private int processString(String str, int index) {
        int skip = 0; // Counter for backspace characters encountered

        while (index >= 0) {
            if (str.charAt(index) == '#') { // If current character is a backspace character
                skip++; // Increment backspace counter
                index--; // Move to the previous character
            } else if (skip > 0) { // If backspace counter is positive
                skip--; // Decrement backspace counter
                index--; // Move to the previous character
            } else { // If current character is a non-backspace character and no backspaces need to be skipped
                break; // Break the loop
            }
        }

        return index; // Return the updated index after processing the string
    }
}