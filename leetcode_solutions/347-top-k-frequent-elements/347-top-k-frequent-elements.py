class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}
        for n in nums:
            mapping[n] = 1 + mapping.get(n, 0)
        
        heap = []
        for key in mapping:
            heappush(heap, (mapping[key], key))
            if len(heap) > k:
                heappop(heap)
                
        # ans = [0] * k
        # i = 0
        # while heap: # O(k)
        #     frq, item = heappop(heap)
        #     ans[i] = item
        #     i += 1
        # return ans
                
        ans = [0] * k
        for i in range(k):
            frq, item = heappop(heap)
            ans[i] = item
            
        return ans
        
        
        
        
        
        

        
# class Solution {
#     public int[] topKFrequent(int[] nums, int k) {
#         Map<Integer, Integer> map = new HashMap<>();
#         for (int n : nums) {
#             map.put(n, map.getOrDefault(n, 0) + 1);
#         }
#         Queue<Integer> heap = new PriorityQueue<>((a,b) -> map.get(a) - map.get(b));
#         for (int n : map.keySet()) {
#             heap.add(n);
#             if (heap.size() > k) heap.poll();
#         }
#         int[] res = new int[k];
#         for (int i = 0; i < k; i++) {
#             res[i] = heap.poll();
#         }
#         return res; 
#     }
    
# }