class Solution {
    public int[] twoSum(int[] nums, int target) {
        int right = nums.length -1;
        int left = 0;
        while(left < right){
            int complement = nums[left] + nums[right];
            System.out.println(complement);
            if(complement > target){
                right--;
            }else if (complement < target){
                left++;
            } else{
                return new int[]{left + 1, right + 1};
            }
        }
        
        return new int[]{-1, -1};
        
    }
}

/*
    [2, 3, 5, 7, 9],  8
     ^           ^

*/