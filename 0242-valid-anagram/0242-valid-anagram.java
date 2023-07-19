class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> map1 = new HashMap<>();
        for(Character c : s.toCharArray()){
            map1.put(c, map1.getOrDefault(c, 0) + 1);
        }
        
        Map<Character, Integer> map2 = new HashMap<>();
        for(Character c : t.toCharArray()){
            map2.put(c, map2.getOrDefault(c, 0) + 1);
        }
        return map1.equals(map2);
    }
}