class Solution {
    public int[] singleNumber(int[] nums) {
        
        Map<Integer, Integer> map = new HashMap<>();
        
        for(Integer n : nums){
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        
        List<Integer> res = new ArrayList<>();
        
        for(Map.Entry<Integer, Integer> entry : map.entrySet()){
            int key = entry.getKey();
            int value = entry.getValue();
            
            if(value == 1){
                res.add(key);
            }
        }
        
        int[] result = new int[res.size()];
        for (int i = 0; i < res.size(); i++) {
            result[i] = res.get(i);
        }

        return result;
    }
}