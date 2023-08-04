class Solution {
    public int longestSubstring(String s, int k) {
        return longestSubstringHelper(s, k, 0, s.length() - 1);
    }
    
    private int longestSubstringHelper(String s, int k, int start, int end) {
        if (end - start + 1 < k) {
            return 0;
        }

        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = start; i <= end; i++) {
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0) + 1);
        }

        for (int mid = start; mid <= end; mid++) {
            if (map.get(s.charAt(mid)) >= k)
                continue;

            int midNext = mid + 1;
            while (midNext <= end && map.get(s.charAt(midNext)) < k) {
                midNext++;
            }

            return Math.max(longestSubstringHelper(s, k, start, mid - 1),
                    longestSubstringHelper(s, k, midNext, end));
        }

        return end - start + 1;
    }
}