public class Solution {
    public int MinInsertions(string s) {
        
        StringBuilder revString = new StringBuilder();
        for (int i = s.Length - 1; i >= 0; i--)
        {
            revString.Append(s[i]);
        }

        if (revString.ToString() == s)
        {
            return 0;
        }
        else
        {
            int minSteps = 0;
            int[,] dp = new int[s.Length, s.Length];

            for (int i = s.Length - 1; i >= 0; i--)
            {
                for (int j = i + 1; j < s.Length; j++)
                {
                    if (s[i] == s[j])
                    {
                        dp[i, j] = dp[i + 1, j - 1];
                    }
                    else
                    {
                        dp[i, j] = Math.Min(dp[i + 1, j], dp[i, j - 1]) + 1;
                    }
                }
            }

            minSteps = dp[0, s.Length - 1];
            return minSteps;
        }
        
    }
}