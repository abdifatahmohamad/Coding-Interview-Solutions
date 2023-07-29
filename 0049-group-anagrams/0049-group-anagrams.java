class Solution {
    int[] charFreq;
    Map<String, List<String>> map;
    public List<List<String>> groupAnagrams(String[] strs) {
        map = new HashMap<>();

        for (String word : strs) {
            charFreq = new int[26];
            for (char c : word.toCharArray()) {
                charFreq[c - 'a']++;
            }

            StringBuilder sb = new StringBuilder();
            for (int count : charFreq) {
                sb.append(count).append('#');
            }

            String key = sb.toString();
            // System.out.println(key);

            if (!map.containsKey(key)) {
                map.put(key, new ArrayList<>());
            }
            map.get(key).add(word);
        }
        
        return new ArrayList<>(map.values());
    }
}