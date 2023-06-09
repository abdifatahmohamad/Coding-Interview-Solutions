public class Solution {
    public char NextGreatestLetter(char[] letters, char target) {
        foreach (char c in letters)
        {
            if (c > target)
            {
                return c;
            }
        }
        
        // return first char if there is nothing greater than the target
        return letters[0];
        
    }
}