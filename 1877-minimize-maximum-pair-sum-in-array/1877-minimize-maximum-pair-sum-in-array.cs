public class Solution {
    
    // O(N Log N) time complexity || O(1) space complexity
    public int MinPairSum(int[] nums) {
        // Sort array in ascending order
        Array.Sort(nums);

        // Using two pointers technique get maximum between current sum and max pair sum.
        int i = 0, j = nums.Length - 1;
        int maxSum = int.MinValue;
        while(i < j){
            maxSum = Math.Max(maxSum, nums[i] + nums[j]);
            i++;
            j--;
        }
        
        return maxSum;
        
    }
}