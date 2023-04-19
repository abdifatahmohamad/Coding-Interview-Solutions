public class Solution {
    public string RemoveDuplicates(string s, int k) {
        
        // Stack with tuple
        Stack<(char, int)> stack = new Stack<(char, int)>();
        foreach (char c in s) {
            if (stack.Count > 0 && stack.Peek().Item1 == c) {
                (char, int) top = stack.Pop();
                if (top.Item2 + 1 < k) {
                    stack.Push((c, top.Item2 + 1));
                }
            } else {
                stack.Push((c, 1));
            }
        }
        StringBuilder sb = new StringBuilder();
        foreach ((char, int) tuple in stack.Reverse()) {
            sb.Append(tuple.Item1, tuple.Item2);
        }
        return sb.ToString();
        
    }
}