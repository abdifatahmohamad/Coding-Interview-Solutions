class Solution {
    public int missingNumber(int[] nums) {
        int total1 = 0; int total2 = 0;
        for(int n: nums){
            total1 += n;
        }
        
        total2 = nums.length * (nums.length + 1) / 2;
        int diff = total2 - total1;
        
        return diff;
        
    }
}