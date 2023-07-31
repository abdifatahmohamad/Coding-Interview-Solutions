class Solution {
    public int mostWordsFound(String[] sentences) {
        int maxLength = Integer.MIN_VALUE;
        for (String sentence : sentences) {
            String[] words = sentence.split(" ");
            int wordCount = words.length;
            // System.out.println(Arrays.toString(words));
            maxLength = Math.max(maxLength, wordCount);
        }
        return maxLength;
    }
}
