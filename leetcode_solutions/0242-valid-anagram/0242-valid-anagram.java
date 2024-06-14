class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        
        Map<Character, Integer> seen = new HashMap<>();
        for(Character c : s.toCharArray()){
            seen.put(c, seen.getOrDefault(c, 0) + 1);
        }
 
        for(Character c : t.toCharArray()){
            if(!seen.containsKey(c) || seen.get(c) < 1){
                return false;
            }else{
                seen.put(c, seen.get(c) - 1);
            }
        }
        
        return true;
    }
}