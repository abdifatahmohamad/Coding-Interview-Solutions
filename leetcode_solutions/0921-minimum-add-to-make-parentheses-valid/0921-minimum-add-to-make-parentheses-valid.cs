public class Solution {
    
    // Solution using stack
    public int MinAddToMakeValid(string s) {
        int res = 0;
        Stack<int> stack = new();
        foreach(var c in s)
        {
            if (c == '(')
            {
                stack.Push(c);
            }
            else
            {
                if (stack.Count > 0)
                {
                    stack.Pop();
                }
                else
                {
                    res++;
                }
            }
        }

        return res + stack.Count;
    }
}