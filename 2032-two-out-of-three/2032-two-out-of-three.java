class Solution {
    public List<Integer> twoOutOfThree(int[] nums1, int[] nums2, int[] nums3) {
        Map<Integer, Integer> map1 = new HashMap<>();
        for(int n : nums1){
            map1.put(n, map1.getOrDefault(n, 0) + 1);
        }

        Map<Integer, Integer> map2 = new HashMap<>();
        for(int n : nums2){
            map2.put(n, map2.getOrDefault(n, 0) + 1);
        }

        Map<Integer, Integer> map3 = new HashMap<>();
        for(int n : nums3){
            map3.put(n, map3.getOrDefault(n, 0) + 1);
        }

        Set<Integer> set = new HashSet<>();
        List<Integer> res = new ArrayList<>();
        for(int key : map1.keySet()){
            if(!set.contains(key) && map2.containsKey(key) || map3.containsKey(key)){
                res.add(key);
                set.add(key);
            }
        }

        for(int key : map2.keySet()){
            if(!set.contains(key) && map3.containsKey(key)){
                res.add(key);
                set.add(key);
            }
        }
        return res;
    }
}