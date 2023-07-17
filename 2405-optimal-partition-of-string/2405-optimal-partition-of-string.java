class Solution {
    public int partitionString(String s) {
        Map<Character, Integer> seen = new HashMap<>();
        // Start result at 1 since we are guarantee that string will not be an empty 
        int res = 1;
        for (char c : s.toCharArray()) {
            // If character in map
            if(seen.containsKey(c)){
                res++;
                // Empty the map
                seen.clear();
            } // If chacarter not in map
            
            // Put that character in the map
            seen.put(c, seen.getOrDefault(c, 0));
        
        }  
        return res;
 
    }
}