class Solution {
    // Min heap
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for(Integer n : nums){
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        // Build priority queue based on lowest to highest frequency (Min heap)       
        PriorityQueue<Integer> pq = new PriorityQueue((a, b) -> map.get(a) - map.get(b));
        for(int key : map.keySet()){
            pq.offer(key);
            if (pq.size() > k) {
                pq.poll(); // Remove elements if the size exceeds k
            }
        }
        int[] res = new int[k];
        int i = k - 1; // Start from the end of the array
        while(i >= 0 && !pq.isEmpty()){
            res[i--] = pq.poll();        
        }
        
        return res;     
    }
    
    // Max heap
    public int[] topKFrequentMaxHeap(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for(Integer n : nums){
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        // Build priority queue based on highest to lowest frequency (Max heap)        
        PriorityQueue<Integer> pq = new PriorityQueue((a, b) -> map.get(b) - map.get(a));
        for(int key : map.keySet()){
            pq.offer(key);
        }
        int[] res = new int[k];
        int i = 0;
        while(k > i){
            if(!pq.isEmpty()){
                res[i++] = pq.poll();
            }
        }
        
        return res;     
    }
    
    
}