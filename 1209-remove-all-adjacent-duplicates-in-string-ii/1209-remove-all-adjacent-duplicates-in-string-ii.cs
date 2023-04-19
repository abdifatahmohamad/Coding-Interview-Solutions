public class Solution {
    public string RemoveDuplicates(string s, int k) {
        
        // Stack with tuple
        var stack = new Stack<(char ch, int count)>();

        foreach (char c in s)
        {
            if (stack.Any() && stack.Peek().ch == c)
            {
                var val = stack.Pop();
                val.count++;
                stack.Push(val);
                if (stack.Peek().count == k)
                {
                    stack.Pop();
                }
            }
            else
            {
                stack.Push((c, 1));
            }

        }

        // String builder
        var res = new StringBuilder();
        while (stack.Any())
        {
            (char c, int count) = stack.Pop();
            res.Insert(0, new string(c, count));
        }

        return res.ToString();
        
    }
}