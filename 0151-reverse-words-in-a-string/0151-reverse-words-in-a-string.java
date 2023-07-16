class Solution {
    public String reverseWords(String s) {
        // Split the input string into an array of words using 
        // one or more whitespace characters as the delimiter
        String[] words = removeStringSpaces(s);
        int left = 0;
        int right = words.length - 1;
        while (left < right) {
            String temp = words[left];
            words[left] = words[right];
            words[right] = temp;
            left++;
            right--;
        }
        
        // Join the reversed words array into a single string using a space as the separator
        return String.join(" ", words);
    }
    
    private static String[] removeStringSpaces(String s) {
        StringBuilder sb = new StringBuilder();
        boolean spaceFlag = false;
        int wordCount = 0;

        // Remove excessive spaces within the string
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c == ' ') {
                if (!spaceFlag) {
                    sb.append(c);
                    spaceFlag = true;
                }
            } else {
                sb.append(c);
                spaceFlag = false;
                if (i == 0 || s.charAt(i - 1) == ' ') {
                    wordCount++;
                }
            }
        }

        // Remove leading spaces
        int start = 0;
        while (start < sb.length() && sb.charAt(start) == ' ') {
            start++;
        }

        // Remove trailing spaces
        int end = sb.length() - 1;
        while (end >= 0 && sb.charAt(end) == ' ') {
            end--;
        }

        // Create array of words
        String resultString = sb.substring(start, end + 1);
        String[] result = resultString.split(" ", wordCount);
        return result;
    }
}