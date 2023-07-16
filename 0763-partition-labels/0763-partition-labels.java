class Solution {
    public List<Integer> partitionLabels(String s) {
        List<Integer> res = new ArrayList<>();
        int[] lastOccurrences = new int[26];

        // Store the last occurrence index of each character
        for (int i = 0; i < s.length(); i++) {
            lastOccurrences[s.charAt(i) - 'a'] = i;
        }

        int start = 0; // Start index of the current partition
        int end = 0; // End index of the current partition

        for (int i = 0; i < s.length(); i++) {
            end = Math.max(end, lastOccurrences[s.charAt(i) - 'a']);

            // If the current index is equal to the end index, we have found a partition
            if (i == end) {
                res.add(end - start + 1);
                start = end + 1; // Move the start index to the next partition
            }
        }

        return res;
    }
}