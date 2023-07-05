public class Solution {
    public int LongestValidParentheses(string s) {   
        int maxCount = 0;
        int lCount = 0;
        int rCount = 0;

        // Scanning the string from left to right to find better maxCount
        for (int i = 0; i < s.Length; i++)
        {
            char c = s[i];
            if (c == '(')
            {
                lCount++;
            }
            else
            {
                rCount++;
            }

            // Check whether we have a valid well-formed string
            if (lCount == rCount)
            {
                // Update the maxium count
                maxCount = Math.Max(maxCount, lCount + rCount);
            }
            else if (rCount > lCount)
            {
                // Reset current progress in our window
                lCount = 0;
                rCount = 0;
            }

        }

        // Reset the pointers to start fresh
        lCount = 0;
        rCount = 0;

        // Scanning the string from right to left to find better maxCount
        // Flip the logic
        for (int i = s.Length - 1; i >= 0; i--)
        {
            char c = s[i];
            if (c == '(')
            {
                lCount++;
            }
            else
            {
                rCount++;
            }

            // Check whether we have a valid well-formed string
            if (lCount == rCount)
            {
                // Update the maxium count
                maxCount = Math.Max(maxCount, lCount + rCount);
            }
            else if (lCount > rCount)
            {
                // Reset current progress in our window
                lCount = 0;
                rCount = 0;
            }

        }



        return maxCount;
        
    }
}