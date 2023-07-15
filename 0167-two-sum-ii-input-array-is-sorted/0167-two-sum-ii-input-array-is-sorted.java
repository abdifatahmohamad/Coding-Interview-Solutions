class Solution {
    public int[] twoSum(int[] nums, int target) {
        int right = nums.length -1;
        int left = 0;
        while(left < right){
            int total = nums[left] + nums[right];
            if(total  == target){
                return new int[]{left + 1, right + 1};
            }else if (total < target){
                left++;
            } else{
                right--;
            }
        }
        
        return new int[]{-1, -1};
        
    }
}

/*
    [2, 3, 5, 7, 9],  8
     ^           ^

*/