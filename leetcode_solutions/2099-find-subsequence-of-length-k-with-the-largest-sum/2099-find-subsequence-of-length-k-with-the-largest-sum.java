class Solution {
    public int[] maxSubsequence(int[] nums, int k) {
        if(k == nums.length){
            return nums;
        }
        
       // Min heap
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int n : nums) {
            pq.offer(n);
            if (pq.size() > k) {
                pq.poll();
            }
        }

        // Create a map to keep track of the count of each element in the heap
        Map<Integer, Integer> map = new HashMap<>();
        for (int n : pq) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }

        List<Integer> resList = new ArrayList<>();
        for (int n : nums) {
            // Check if the element is present in the map and has a count > 0
            if (map.containsKey(n) && map.get(n) > 0) {
                // Decrease the count in the counter map
                map.put(n, map.get(n) - 1);
                resList.add(n);
            }
        }

        // Convert the resList list to an array
        int[] ans = new int[resList.size()];
        for (int i = 0; i < resList.size(); i++) {
            ans[i] = resList.get(i);
        }
        return ans;
    }
}