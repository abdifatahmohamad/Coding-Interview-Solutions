public class Solution {
    public bool CheckRecord(string s) {
        
        int absenceCount = 0;
        int consecutiveLates = 0;

        foreach (char c in s)
        {
            if (c == 'A')
            {
                absenceCount++;
                if (absenceCount >= 2)
                {
                    return false;
                }
            }

            if (c == 'L')
            {
                consecutiveLates++;
                if (consecutiveLates >= 3)
                {
                    return false;
                }
            }
            else
            {
                consecutiveLates = 0; // Reset the count if it's not 'L'
            }
        }

        return true;
        
    }
}