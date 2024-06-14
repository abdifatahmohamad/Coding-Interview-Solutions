class Solution {
    public String frequencySort(String s) {
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            map.merge(s.charAt(i), 1, Integer::sum);
        }

        // Create a list of unique characters from the map
        List<Character> chars = new ArrayList<>(map.keySet());

        // Sort the characters based on their frequencies in descending order
        Collections.sort(chars, (a, b) -> map.get(b) - map.get(a));

        // Build the result string based on the sorted characters and their frequencies
        StringBuilder sb = new StringBuilder();
        for (char c : chars) {
            int freq = map.get(c);

            // Append the character to the result string 'freq' times
            while (freq-- > 0) {
                sb.append(c);
            }
        }

        // Return the final result as a string
        return sb.toString();
    }
}