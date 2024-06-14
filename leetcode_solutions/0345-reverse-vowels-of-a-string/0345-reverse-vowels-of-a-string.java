class Solution {
    public String reverseVowels(String s) {
        // Convert the input string to a character array
        char[] chars = s.toCharArray();
        int start = 0;
        int end = chars.length - 1;
        reverseVowels(chars, start, end);
        // Convert the modified character array back to a string
        return new String(chars);
        
    }
    
    // Helper method that reverses vowels
    private static void reverseVowels(char[] chars, int start, int end) {
        // Array of vowel characters
        char[] vowels = {'a', 'e', 'i', 'o', 'u'};
        // Iterate until the start pointer crosses the end pointer
        while (start < end) {
            if (isVowel(chars[start], vowels) && isVowel(chars[end], vowels)) {
                // If both the start and end characters are vowels, swap them
                char temp = chars[start];
                chars[start] = chars[end];
                chars[end] = temp;
                start++;
                end--;
            } else if (isVowel(chars[start], vowels)) {
                // If the start character is a vowel and the end character is not, 
                // move the end pointer towards the center
                end--;
            } else {
                // If the start character is not a vowel, 
                // move the start pointer towards the center
                start++;
            }
        }
    }
    
    private static boolean isVowel(char c, char[] vowels) {
         // Convert the character to lowercase
        c = Character.toLowerCase(c);
        for (char vowel : vowels) {
            if (vowel == c) {
                // If the character matches a vowel in the array, return true
                return true; 
            }
        }
        return false; 
    }
}