class Solution {
    public int partitionString(String s) {
        Set<Character> seen = new HashSet();
        // Start result at 1 since we are guarantee that string will not be an empty 
        int res = 1;
        for (char c : s.toCharArray()) {
            // If character in map
            if(seen.contains(c)){
                res++;
                // Empty the map
                seen.clear();
            } // If chacarter not in map
            
            // Put that character in the map
            seen.add(c);
        
        }  
        return res;
 
    }
}