class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        
        // Create a HashMap to store the frequencies of each number
        Map<Integer, Integer> map = new HashMap<>();

        // Iterate over the input array and update the frequencies in the map
        for (int n : nums) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }

        // Create a PriorityQueue with a custom comparator to order elements by their frequencies
        // PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.comparingInt(map::get));
        // PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.comparingInt(key -> map.get(key)));
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> map.get(a) - map.get(b));



        // Iterate over the keys in the map and add them to the priority queue
        // Keep the size of the priority queue limited to 'k'
        for (int key : map.keySet()) {
            pq.offer(key);
            if (pq.size() > k) {
                pq.poll();
            }
        }

        // Create an array to store the top 'k' frequent elements
        int[] res = new int[k];

        // Populate the result array in reverse order by polling elements from the priority queue
        for (int i = k - 1; i >= 0; i--) {
            res[i] = pq.poll();
        }

        // Return the result array
        return res;
        
    }
}