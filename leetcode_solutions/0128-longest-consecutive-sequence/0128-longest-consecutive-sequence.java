class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            seen.add(num);
        }

        int res = Integer.MIN_VALUE;
        for (int num : nums) {
            if (!seen.contains(num - 1)) {
                int count = 1;
                while (seen.contains(num + count)) {
                    count++;
                }
                res = Math.max(res, count);
            }
        }
        return res;   
    }
}