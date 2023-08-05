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

        int cycles = 0;
        while (!maxHeap.isEmpty()) {
            List<Integer> temp = new ArrayList<>();
            for (int i = 0; i < n + 1; i++) {
                if (!maxHeap.isEmpty()) {
                    temp.add(maxHeap.poll() - 1);
                }
            }

            for (int num : temp) {
                if (num > 0) {
                    maxHeap.offer(num);
                }
            }

            cycles += maxHeap.isEmpty() ? temp.size() : n + 1;
        }

        return cycles;
    }
}

/*

freq / n
3 

*/