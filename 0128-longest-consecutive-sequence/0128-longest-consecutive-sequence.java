class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length == 0){
            return 0;
        }
        Map<Integer, Integer> map = new HashMap<>();
        for(int n : nums){
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        
         // Step 2: Sort the values of the HashMap
        List<Integer> sortedValues = new ArrayList<>(map.keySet());
        Collections.sort(sortedValues);

        // Find the longest consecutive sequence
        int res = 0;

        for (int num : map.keySet()) {
            if (!map.containsKey(num - 1)) {
                int curr = 1;

                while (map.containsKey(num + 1)) {
                    num++;
                    curr++;
                }

                res = Math.max(res, curr);
            }
        }

        
        return res;
        
    }
}