class Solution {
    public boolean checkAlmostEquivalent(String word1, String word2) {
        if (word1.length() != word2.length()) {
            return false;
        }

        Map<Character, Integer> map1 = new HashMap<>();
        Map<Character, Integer> map2 = new HashMap<>();

        // Build character frequency maps for both words in a single loop
        for (int i = 0; i < word1.length(); i++) {
            char c1 = word1.charAt(i);
            char c2 = word2.charAt(i);

            map1.put(c1, map1.getOrDefault(c1, 0) + 1);
            map2.put(c2, map2.getOrDefault(c2, 0) + 1);
        }

        int count = 0;
        for (char k : map1.keySet()) {
            if (map2.containsKey(k)) {
                if (Math.abs(map1.get(k) - map2.get(k)) > 3) {
                    count++;
                    break;
                }
            } else if (map1.get(k) > 3) {
                count++;
                break;
            }
        }

        for (char k : map2.keySet()) {
            if (!map1.containsKey(k) && map2.get(k) > 3) {
                count++;
                break;
            }
        }

        return count == 0;
        
    }
}