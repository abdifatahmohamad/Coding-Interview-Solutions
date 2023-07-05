public class Solution {
    public int MinPairSum(int[] nums) {
        int[] bucket = new int[nums.Max() + 1];
        foreach (int n in nums)
        {
            bucket[n]++;
        }

        return GetMinPairSum(bucket);
         
    }
    
    
    // Method that gets the max per sum
    public static int GetMinPairSum(int[] bucket)
    {
        int i = 1;
        int j = bucket.Length - 1;
        int maxSum = int.MinValue;

        while (i < j)
        {
            if (bucket[i] != 0 && bucket[j] != 0)
            {
                maxSum = Math.Max(maxSum, i + j);
                bucket[i]--;
                bucket[j]--;
            }

            if (bucket[i] == 0)
                i++;

            if (bucket[j] == 0)
                j--;
        }
        
        if (bucket[i] == bucket[j]) {
            maxSum = Math.Max(maxSum, i + j);
        }

        return maxSum;
    }
}