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

        // Initialize a variable to keep track of the total cycles needed to complete all tasks.
        int cycles = 0;
        while (!maxHeap.isEmpty()) {
            // Create a temporary list to store tasks that will be executed in the current cycle.
            List<Integer> temp = new ArrayList<>();

            // Execute tasks for (n + 1) cycles, where n is the cooldown period.
            for (int i = 0; i < n + 1; i++) {
                if (!maxHeap.isEmpty()) {
                    // Pop the task with the highest frequency from the max heap and decrement its count.
                    temp.add(maxHeap.poll() - 1);
                }
            }

            // Add back the remaining tasks (with decreased frequency) to the max heap.
            for (int num : temp) {
                if (num > 0) {
                    maxHeap.offer(num);
                }
            }

            // If the max heap becomes empty, there are no more tasks to execute.
            // Increment cycles by the number of remaining tasks in the temporary list.
            // Otherwise, increment cycles by (n + 1), because (n + 1) tasks will be executed in this cycle.
            cycles += maxHeap.isEmpty() ? temp.size() : n + 1;
        }

        // Return the total cycles needed to finish all tasks.
        return cycles;
    }
}

/*

freq / n
3 

*/