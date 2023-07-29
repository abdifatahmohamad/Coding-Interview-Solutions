class Solution {
    Map<Integer, Integer> map;
    PriorityQueue<Integer> maxHeap;
    // Solution uses maxHeap
    public int[] topKFrequent(int[] nums, int k) {
        map = new HashMap<>();
        for(int n : nums){
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        maxHeap = new PriorityQueue<Integer>((a, b) -> map.get(b) - map.get(a));
        for(int key : map.keySet()){
            maxHeap.offer(key);
        }
        
        int[] res = new int[k];
        int i = 0;
        while(k > i){
            if(!maxHeap.isEmpty()){
                res[i++] = maxHeap.poll();
            }
        }  
        return res;
    }
}