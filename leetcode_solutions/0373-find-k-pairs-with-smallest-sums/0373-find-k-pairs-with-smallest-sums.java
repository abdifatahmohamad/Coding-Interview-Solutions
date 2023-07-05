class Solution {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        List<List<Integer>> result = new ArrayList<>();

        // Edge cases
        if (nums1 == null || nums1.length == 0 || nums2 == null || nums2.length == 0 || k <= 0)
            return result;

        // Use a min heap to store the pairs based on the sum
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] + a[1] - b[0] - b[1]);

        // Populate the min heap
        for (int i = 0; i < nums1.length && i < k; i++) {
            pq.offer(new int[]{nums1[i], nums2[0], 0});
        }

        // Process the k smallest pairs
        while (k-- > 0 && !pq.isEmpty()) {
            int[] current = pq.poll();
            int num1 = current[0];
            int num2 = current[1];
            int index = current[2];
            result.add(List.of(num1, num2));

            // Add the next pair from nums2 for the current num1
            if (index + 1 < nums2.length) {
                pq.offer(new int[]{num1, nums2[index + 1], index + 1});
            }
        }

        return result;
    }
}
