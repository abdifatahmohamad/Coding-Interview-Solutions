class Solution {
    public int findLHS(int[] nums) {
        // https://www.youtube.com/watch?v=tgkpqp5-6Os
        Map<Integer, Integer> map = new HashMap<>();
        for (int n : nums) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        
        int longest = 0;
        for (int key : map.keySet()) {
            if (map.containsKey(key + 1)) {
                longest = Math.max(longest, 
                          map.get(key) + map.get(key + 1));
            }
        }
        
        return longest;
        
    }
}