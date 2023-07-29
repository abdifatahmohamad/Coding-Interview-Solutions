class Solution {
    Map<Integer, Integer> map;
    PriorityQueue<Integer> minHeap;
    public int[] topKFrequent(int[] nums, int k) {
        map = new HashMap<>();
        for(int n : nums){
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        minHeap = new PriorityQueue<>((a, b) -> map.get(a) - map.get(b));
        for(int key : map.keySet()){
            minHeap.offer(key);
            if(minHeap.size() > k){
                minHeap.poll();
            }
        }
        
        int[] res = new int[k];
        int i = 0;
        while(k > i){
            if(!minHeap.isEmpty()){
               res[i++] = minHeap.poll(); 
            } 
        }
        return res;
    }
}