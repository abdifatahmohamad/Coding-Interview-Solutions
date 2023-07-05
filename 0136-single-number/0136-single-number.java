class Solution {
    public int singleNumber(int[] nums) {
        Map<Integer, Integer> map = new LinkedHashMap<>();
        
        for(Integer n : nums){
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        
        for(Map.Entry<Integer, Integer> entry : map.entrySet()){
            int key = entry.getKey();
            int value = entry.getValue();
            
            if(value == 1){
                return key;
            }
        }
        
        return -1;
        
    }
}