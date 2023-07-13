class Solution {
    public String reverseVowels(String s) {
        char[] chars = s.toCharArray();
        int start = 0;
        int end = chars.length - 1;

        reverseVowelsInRange(chars, start, end);

        return new String(chars);
        
    }
    
    private static void reverseVowelsInRange(char[] chars, int start, int end) {
        char[] vowels = {'a', 'e', 'i', 'o', 'u'};

        while (start < end) {
            if (isVowel(chars[start], vowels) && isVowel(chars[end], vowels)) {
                // Swap the vowels
                char temp = chars[start];
                chars[start] = chars[end];
                chars[end] = temp;
                start++;
                end--;
            } else if (isVowel(chars[start], vowels)) {
                end--;
            } else {
                start++;
            }
        }
    }
    
    private static boolean isVowel(char c, char[] vowels) {
        c = Character.toLowerCase(c);
        for (char vowel : vowels) {
            if (vowel == c) {
                return true;
            }
        }
        return false;
    }
}