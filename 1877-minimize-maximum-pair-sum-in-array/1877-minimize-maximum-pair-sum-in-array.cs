public class Solution {
    public int MinPairSum(int[] nums) {
        
        Array.Sort(nums);
        
        int[] sortedArray = nums;
        
        int i = 0;
        int j = sortedArray.Length - 1;
        int maxSum = int.MinValue;
        while(i < j){
            maxSum = Math.Max(maxSum, sortedArray[i] + sortedArray[j]);
            i++;
            j--;
        }
        
        return maxSum;
        
    }
}