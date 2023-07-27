class Solution {
    public boolean checkAlmostEquivalent(String word1, String word2) {
        if (word1.length() != word2.length()) {
            return false;
        }

        Map<Character, Integer> map1 = new HashMap<>();
        for (char c : word1.toCharArray()) {
            map1.put(c, map1.getOrDefault(c, 0) + 1);
        }

        Map<Character, Integer> map2 = new HashMap<>();
        for (char c : word2.toCharArray()) {
            map2.put(c, map2.getOrDefault(c, 0) + 1);
        }

        int res = 0;
        for (char k : map1.keySet()) {
            if (map2.containsKey(k)) {
                if (Math.abs(map1.get(k) - map2.get(k)) > 3) {
                    res++;
                    break;
                }
            } else if (map1.get(k) > 3) {
                res++;
                break;
            }
        }

        for (char k : map2.keySet()) {
            if (map1.containsKey(k)) {
                if (Math.abs(map1.get(k) - map2.get(k)) > 3) {
                    res++;
                    break;
                }
            } else if (map2.get(k) > 3) {
                res++;
                break;
            }
        }

        return res == 0;
    }
}