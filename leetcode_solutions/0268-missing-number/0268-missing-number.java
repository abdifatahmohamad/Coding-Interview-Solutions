class Solution {
    public int missingNumber(int[] nums) {
        int missing = nums.length;
        
        for(int i = 0; i < nums.length; i++){
            
            missing ^= nums[i] ^ i;
            
            /**        
            missing = 3
            i = [0, 1, 2]
            nums[i] = [3, 0, 1]
            
            So,
                  3
                XOR
                  [0, 1, 2]
                XOR
                  [3, 0, 1]
              ---------------
                     2  
            */
        }
        
        return missing;
        
    }
}