class Solution {
    public int[] singleNumber(int[] nums) {
        
        Map<Integer, Integer> map = new HashMap<>();
        
        for(Integer n : nums){
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        
    
        int valueCount = 0;
        for(int val : map.values()){
            if(val == 1){
                valueCount++;
            }
        }
        
        int[] res = new int[valueCount];
        int idx = 0;
        for(Map.Entry<Integer, Integer> entry : map.entrySet()){
            int key = entry.getKey();
            int value = entry.getValue();
            
            if(value == 1){
                res[idx++] = key;
            }
        }
        

        return res;
    }
}