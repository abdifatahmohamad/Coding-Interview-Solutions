public class Solution {
    public int LongestPalindrome(string s) {
        if(s.Length == 1){
            return 1;
        }
        
        // Dictionary<char, int> map = new();
        Dictionary<char, int> map = new(26 * 26); // Tachnically constant 52 uppder & lower case characters

        foreach (char ch in s){
            map[ch] = map.GetValueOrDefault(ch, 0) + 1;
        }
        
        int res = 0;
        bool hasOdd = false;
        foreach (var kvp in map){
            char key = kvp.Key;
            int value =  kvp.Value;
            if(value % 2 == 0){
                res += value;
            } else{
                res += value - 1;
                hasOdd = true;
            }
        }
        
        if(hasOdd){
            res++;
        }
        
        return res;
        
    }
}