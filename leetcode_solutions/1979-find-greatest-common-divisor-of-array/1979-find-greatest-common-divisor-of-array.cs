public class Solution {
    public int FindGCD(int[] nums) {
        int minVal = nums.Min();
        int maxVal = nums.Max();
        
        return GetGreatestCommonDivisor(minVal, maxVal);
        
    }
    
    static int GetGreatestCommonDivisor(int num1, int num2)
    {
        while (num2 != 0)
        {
            int temp = num2;
            num2 = num1 % num2;
            num1 = temp;
        }

        return num1;
    }
}