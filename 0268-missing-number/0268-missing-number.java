class Solution {
    public int missingNumber(int[] nums) {
        HashMap<Integer, Integer> mp = new HashMap<Integer, Integer>();
        for(int i=0; i<nums.length; i++){
            mp.put(nums[i], i);
        }
        for(int i=0; i<=nums.length; i++){
            if(!mp.containsKey(i)){
                return i;
            } 
        }
        return 0;
        
    }
}