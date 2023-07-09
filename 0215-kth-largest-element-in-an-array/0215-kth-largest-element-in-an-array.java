class Solution {
    public int findKthLargest(int[] nums, int k) {
        // Convert array into max heap
        PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>((a, b) -> (b - a));
        for(int n : nums){
            maxHeap.offer(n);
        }

        int res = 0;
        int i = 0;
        while(k > i++){
            if(!maxHeap.isEmpty()){
                res = maxHeap.poll();
            }
        }
        
        return res;
        
    }
}

/*
[3,2,3,1,2,4,5,5,6]

[1, 2, 2, 3, 3, 4, 5, 5, 6]

*/