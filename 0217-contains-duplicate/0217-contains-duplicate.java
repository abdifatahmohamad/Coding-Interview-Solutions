class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for(Integer n : nums){
            map.put(n, map.getOrDefault(n, 0) +  1);
        }
        
        for(Map.Entry<Integer, Integer> entry : map.entrySet()){
            int key = entry.getKey();
            int value = entry.getValue();
            if(value > 1){
                return true;
            }
        }
        

        
        return false;
        
    }
}