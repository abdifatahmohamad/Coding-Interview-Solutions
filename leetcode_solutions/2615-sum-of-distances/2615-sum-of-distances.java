class Solution {
    public long[] distance(int[] nums) {
        int n = nums.length;
        Map<Integer, Long> seen = new HashMap<>();
        Map<Integer, Long> count = new HashMap<>();
        long[] res = new long[n];
        
        for (int i = 0; i < n; i++) {
            res[i] += (count.getOrDefault(nums[i], 0L) * i) - seen.getOrDefault(nums[i], 0L);
            seen.put(nums[i], seen.getOrDefault(nums[i], 0L) + i);
            count.put(nums[i], count.getOrDefault(nums[i], 0L) + 1);
        }
        
        seen.clear();
        count.clear();
        for (int i = n - 1; i >= 0; i--) {
            res[i] += seen.getOrDefault(nums[i], 0L) - (count.getOrDefault(nums[i], 0L) * i);
            seen.put(nums[i], seen.getOrDefault(nums[i], 0L) + i);
            count.put(nums[i], count.getOrDefault(nums[i], 0L) + 1);
        }
        
        return res;
    }
}