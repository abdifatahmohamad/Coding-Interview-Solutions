public class Solution {
    public string LongestNiceSubstring(string s) {
        int n = s.Length;
        int maxLength = 0; 
        int maxStart = 0; int maxEnd = 0;

        for (int l = 0; l < n; l++) {
            int r = l + 1;
            while (r <= n) {
                string substr = s.Substring(l, r - l);
                if (IsNice(substr) && substr.Length > maxLength) {
                    maxLength = substr.Length;
                    maxStart = l;
                    maxEnd = r;
                }
                r++;
            }
        }

        return s.Substring(maxStart, maxEnd - maxStart);
    }

    // Helper method
    private bool IsNice(string s) {
        var unique = new HashSet<char>(s);
        foreach (char ch in unique) {
            if (!unique.Contains(char.ToLower(ch)) || !unique.Contains(char.ToUpper(ch))) {
                return false;
            }
        }
        return true;
    }
}
