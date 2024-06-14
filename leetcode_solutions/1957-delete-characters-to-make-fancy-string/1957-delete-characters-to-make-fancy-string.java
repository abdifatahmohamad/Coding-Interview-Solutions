class Solution {
    public String makeFancyString(String s) {     
        if (s == null || s.length() < 2) {
            return s;
        }

        StringBuilder sb = new StringBuilder();
        char prevChar = s.charAt(0); // Track the previous character
        int count = 1; // Track the count of consecutive occurrences of the character

        sb.append(prevChar); // Append the first character to the StringBuilder

        for (int i = 1; i < s.length(); i++) {
            char currChar = s.charAt(i);

            if (currChar == prevChar) {
                count++;

                if (count > 2) {
                    continue; // Skip appending the character if count > 2
                }
            } else {
                count = 1; // Reset the count for a new character
            }

            sb.append(currChar); // Append the character to the StringBuilder
            prevChar = currChar; // Update the previous character
        }

        return sb.toString();
        
    }
}