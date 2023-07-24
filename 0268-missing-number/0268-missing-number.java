class Solution {
    public int missingNumber(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int n : nums){
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        
        for(int key : map.keySet()){
            System.out.println(key + ":" + map.get(key));
        }
        
        int missing = 0;
        for(int i = 0; i < nums.length + 1; i++){
            
            if(!map.containsKey(i)){
                missing = i;
            }
            // System.out.println(i);
        }
        
        return missing;
        
    }
}