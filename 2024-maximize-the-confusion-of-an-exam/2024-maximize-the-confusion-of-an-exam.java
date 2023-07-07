class Solution {
    public int maxConsecutiveAnswers(String answerKey, int k) {
        int n = answerKey.length();
        int maxConfusion = 0;
        int left = 0;
        int maxCount = 0;
        int[] freq = new int[26]; // Frequency array to track character counts
        
        for (int right = 0; right < n; right++) {
            char curr = answerKey.charAt(right);
            freq[curr - 'A']++; // Increment the frequency of the current character
            
            // Update maxCount with the maximum frequency of any character
            maxCount = Math.max(maxCount, freq[curr - 'A']);
            
            // Calculate the number of characters to change (non-'T' characters)
            int changes = (right - left + 1) - maxCount;
            
            // If the number of changes exceeds k, move the left pointer
            if (changes > k) {
                char leftChar = answerKey.charAt(left);
                freq[leftChar - 'A']--; // Decrement the frequency of the left character
                left++; // Move the left pointer
            }
            
            // Update maxConfusion with the maximum length of the window
            maxConfusion = Math.max(maxConfusion, right - left + 1);
        }
        
        return maxConfusion;
        
    }
}