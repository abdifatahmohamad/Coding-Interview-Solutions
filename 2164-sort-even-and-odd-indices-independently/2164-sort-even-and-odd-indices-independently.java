class Solution {
    public int[] sortEvenOdd(int[] nums) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);

        for (int i = 0; i < nums.length; i++) {
            if (i % 2 == 0) {
                minHeap.offer(nums[i]);
            } else {
                maxHeap.offer(nums[i]);
            }
        }
        
        int[] res = new int[nums.length];
        int i = 0;
        while (!minHeap.isEmpty() && !maxHeap.isEmpty()) {
            res[i++] = minHeap.poll();
            res[i++] = maxHeap.poll();
        }
        
        while (!minHeap.isEmpty()) {
            res[i++] = minHeap.poll();
        }
        while (!maxHeap.isEmpty()) {
            res[i++] = maxHeap.poll();
        }
        
        return res;
    }
}