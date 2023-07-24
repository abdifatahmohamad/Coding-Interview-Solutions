class Solution {
    public int firstMissingPositive(int[] nums) {
        Map<Integer, Boolean> map = new HashMap<>();
        for(int n : nums){
            if(n > 0){
                map.put(n, true);
            }
        }
        
//         for(int key : map.keySet()){
//             System.out.println(key + ":" + map.get(key));
//         }
        
//         System.out.println("-------");
        
//         for(int i = 0; i < nums.length; i++){
//             System.out.println("i: " + i + " num: " + nums[i]);
//         }
        
        // Number 1 is the smallest positive integer
        int missing = 1;
        while(map.containsKey(missing)){
            missing++;
        }
        return missing;
        
    }
}