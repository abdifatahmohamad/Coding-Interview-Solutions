class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for(Integer n : nums){
            map.put(n, map.getOrDefault(n, 0) +  1);
        }
        
        for(Map.Entry<Integer, Integer> entry : map.entrySet()){
            int key = entry.getKey();
            int value = entry.getValue();
            
            if(value > nums.length / 2){
                return key;
            }
        }
        
        return -1;
        
    }
}