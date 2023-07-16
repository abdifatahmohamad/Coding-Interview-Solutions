class Solution {
    public int partitionString(String s) {
        Map<Character, Integer> seen = new HashMap<>();
        // Start result at 1 since we are guarantee that string will not be an empty 
        int res = 1;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            // If character in map
            if(seen.containsKey(c)){
                res++;
                // Empty the map
                seen.clear();
                // Put that character in the map
                seen.put(c, seen.getOrDefault(c, 0));
            } // If chacarter not in map
            else{
                // Put that character in the map
                seen.put(c, seen.getOrDefault(c, 0));
            }
        }  
        return res;
 
    }
}