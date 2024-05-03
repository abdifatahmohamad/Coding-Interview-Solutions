using System;
using System.Collections.Generic;

public class Solution {
    public int FindMaxK(int[] nums) {
        Dictionary<int, int> mapping = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++) {
            mapping[nums[i]] = i;
        }
        int maxVal = int.MinValue;
        foreach (int k in mapping.Keys) {
            if (mapping.ContainsKey(-k)) {
                maxVal = Math.Max(maxVal, k);
            }
        }
        return maxVal != int.MinValue ? maxVal : -1;
    }
}
