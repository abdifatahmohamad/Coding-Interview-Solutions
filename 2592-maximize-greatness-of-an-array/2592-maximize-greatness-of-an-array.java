class Solution {
    public int maximizeGreatness(int[] nums) {
        // Convert array into min heap - min heap is built-in in java by default
        PriorityQueue<Integer> pq1 = new PriorityQueue<Integer>();
        PriorityQueue<Integer> pq2 = new PriorityQueue<Integer>();
        for(int n : nums){
            pq1.offer(n);
            pq2.offer(n);
        }

        // Print the elements in the PriorityQueue
        // while (!pq1.isEmpty()) {
        //     System.out.print(pq1.poll() + " ");
        // }
        
        // Compare both heaps and find count of elements that are greater in pq1
        int count = 0;
        while (!pq2.isEmpty()) {
            int val1 = pq1.peek();
            int val2 = pq2.peek();

            if (val1 < val2) {
                pq1.poll(); // Remove the smaller value from pq1
                count++;
            }
            pq2.poll();// Remove the smaller value from pq2        
        }
        return count;      
    }
}