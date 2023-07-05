public class Solution {
    public string CustomSortString(string order, string s) {
        
        Dictionary<char, int> count = new Dictionary<char, int>();
        foreach (char c in s) {
            if (count.ContainsKey(c)) {
                count[c]++;
            } else {
                count.Add(c, 1);
            }
        }

        List<char> res = new List<char>();
        foreach (char ch in order) {
            if (count.ContainsKey(ch)) {
                for (int i = 0; i < count[ch]; i++) {
                    res.Add(ch);
                }
                count.Remove(ch);
            }
        }

        // add remaining characters to the result list in any order
        foreach (KeyValuePair<char, int> pair in count) {
            for (int i = 0; i < pair.Value; i++) {
                res.Add(pair.Key);
            }
        }

        return new string(res.ToArray());        
    }
}