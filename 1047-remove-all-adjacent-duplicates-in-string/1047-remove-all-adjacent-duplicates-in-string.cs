public class Solution {
    public string RemoveDuplicates(string s) {
        Stack<Char> stack = new();

        foreach (char c in s)
        {
            if (stack.Count > 0 && stack.Peek() == c)
            {
                stack.Pop();
            }
            else
            {
                stack.Push(c);
            }
        }


        return string.Join("", stack.Reverse());
    }
}