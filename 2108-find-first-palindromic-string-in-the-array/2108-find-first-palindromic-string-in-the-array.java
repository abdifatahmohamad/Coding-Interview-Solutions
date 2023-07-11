class Solution {
    public String firstPalindrome(String[] words) {
        for (String s : words) {
            int right = s.length() - 1;
            int left = 0;
            while (left < right) {
                if (s.charAt(left) != s.charAt(right)) {
                    break; // Not a palindrome, break out of the loop
                }
                left++;
                right--;
            }
            if (left >= right) {
                return s; // Palindrome found, return it
            }
        }
        return ""; // No palindrome found
    }
}