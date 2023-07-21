class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length == 0){
            return 0;
        }
        Map<Integer, Integer> map = new HashMap<>();
        for(int n : nums){
            map.put(n, map.getOrDefault(n, 0) + 1);
        }

        // Find the longest consecutive sequence
        int res = 0;
        
        // Loop through the distinct elements in the map
        for (int n : map.keySet()) {
            // Check if the previous consecutive number exists in the map
            if (!map.containsKey(n - 1)) {
                // If not, start counting the consecutive sequence for that element
                int curr = 1;
        // Continue counting the consecutive sequence until there is no next consecutive number
                while (map.containsKey(n + 1)) {
                    n++;
                    curr++;
                }

                res = Math.max(res, curr);
            }
        }

        
        return res;
        
    }
}