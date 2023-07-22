class Solution {
    public int longestConsecutive(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int n : nums){
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        int res = 0;
        for (int n : map.keySet()) {
            // Check if i's the start of a sequence
            if(!map.containsKey(n - 1)){
                int length = 0;
                while (map.containsKey(n + length)) {
                    length++;
                }

                res = Math.max(res, length);
                
            }
        }    
        return res;      
    }
}