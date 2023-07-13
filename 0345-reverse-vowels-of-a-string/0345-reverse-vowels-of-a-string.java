class Solution {
    public String reverseVowels(String s) {
        char[] chars = s.toCharArray();
        int start = 0;
        int end = chars.length - 1;

        reverseVowelsInRange(chars, start, end);

        return new String(chars);
        
    }
    
    private static void reverseVowelsInRange(char[] chars, int start, int end) {
        while (start < end) {
            if (isVowel(chars[start]) && isVowel(chars[end])) {
                // Swap the vowels
                char temp = chars[start];
                chars[start] = chars[end];
                chars[end] = temp;
                start++;
                end--;
            } else if (isVowel(chars[start])) {
                end--;
            } else {
                start++;
            }
        }
    }
    
    private static boolean isVowel(char c) {
        c = Character.toLowerCase(c);
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}