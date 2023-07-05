public class Solution {
           public  string MinRemoveToMakeValid(string s)
        {
            StringBuilder res = new StringBuilder();
            Stack<int> stack = new ();
            int lastIndex = 0;
            for (int i = 0; i < s.Length; i++)
            {
                char c = s[i];
                if (c == ')' && stack.Count == 0){
                    continue;
                }
                
                if (c == ')'){
                    stack.Pop();
                }
                
                if (c == '('){
                    stack.Push(lastIndex);
                }
                
                res.Append(c);
                lastIndex++;
            }
               
  
            if (stack.Count > 0)
            {
                while (stack.Count > 0)
                {
                    res = res.Remove(stack.Pop(), 1);
                }
            }
               
            return res.ToString();
        }
}