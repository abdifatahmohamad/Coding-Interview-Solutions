class Solution {
    public int findLHS(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int n : nums) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        
        int longest = 0;
        for (int key : map.keySet()) {
            // Get the count of occurrences 
            int count = map.get(key);
            // System.out.println(key + ":" + count);
        // Check if the next number (num + 1) exists in the map
            if (map.containsKey(key + 1)) {
                int currentLHS = count + map.get(key + 1);
                // System.out.println(currentLHS);
                // Calculate the LHS starting with n
                longest = Math.max(longest, currentLHS);
            }
        }
        
        return longest;
        
    }
}