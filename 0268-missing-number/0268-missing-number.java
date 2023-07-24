class Solution {
    public int missingNumber(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int n : nums){
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        
        for(int i = 0; i <= nums.length; i++){
            if(!map.containsKey(i)){
                return i;
            }
        }   
        return 0;      
    }
}