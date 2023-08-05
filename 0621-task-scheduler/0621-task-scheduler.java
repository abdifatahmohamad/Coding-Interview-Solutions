class Solution {
    public int leastInterval(char[] tasks, int n) {
        if(n == 0){
            return tasks.length;
        }
        
        Map<Character, Integer> map = new HashMap<>();
        for (char c : tasks) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        
        PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>((a, b) -> (b - a));
        for(int num : map.values()){
            maxHeap.offer(num);
        }

        // Get the maximum frequency from the max heap.
        int maxNum = maxHeap.peek();

        int i = 0, maxTaskCounter = 0;
        // Find how many tasks have the maximum frequency.
        while (!maxHeap.isEmpty() && maxHeap.peek() == maxNum) {
            maxTaskCounter++;
            maxHeap.poll();
        }

        // Apply the formula to calculate intervals as derived from the Python code.
        int intervals = (maxNum - 1) * (n + 1) + maxTaskCounter;

        // The formula doesn't hold for some cases like (ABCABCDEFG),
        // so we take the max of intervals and the total number of tasks to get the final answer.
        return Math.max(intervals, tasks.length);
    }
}

/*

freq / n
3 

*/