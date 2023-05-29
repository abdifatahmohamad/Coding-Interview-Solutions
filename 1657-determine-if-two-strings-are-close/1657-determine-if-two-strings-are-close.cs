public class Solution {
    public bool CloseStrings(string word1, string word2) {
        
        if(word1.Length != word2.Length){
            return false;
        }
        
        // var map = new Dictionary<char, int>();
        Dictionary<char, int> map1 = new();
        foreach (char c in word1)
        {
            map1[c] = map1.GetValueOrDefault(c, 0) + 1;
        }

        Dictionary<char, int> map2 = new Dictionary<char, int>();
        foreach (char c in word2)
        {
            map2[c] = map2.GetValueOrDefault(c, 0) + 1;
        }

        var keys1 = map1.Keys.OrderBy(k => k);
        var keys2 = map2.Keys.OrderBy(k => k);

        var values1 = map1.Values.OrderBy(v => v);
        var values2 = map2.Values.OrderBy(v => v);
    
        return keys1.SequenceEqual(keys2) && values1.SequenceEqual(values2); 

    }
}


/*

"abc"
"bca"
"a"
"aa"
"cabbba"
"abbccc"
"aaabbbbb"
"aaaaabbb"
"abc"
"bca"

*/