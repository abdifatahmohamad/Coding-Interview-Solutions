class Solution {
    int[] charFreq;
    Map<String, List<String>> map;
    public List<List<String>> groupAnagrams(String[] strs) {
        map = new HashMap<>();

        for (String word : strs) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String sortedStr = String.valueOf(chars);
            if (!map.containsKey(sortedStr)) {
                map.put(sortedStr, new ArrayList<>());
            }
            map.get(sortedStr).add(word);
        }
        
        return new ArrayList<>(map.values());
    }
}