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

        List<int> value1 = new List<int>(map1.Values);
        List<int> value2 = new List<int>(map2.Values);
        List<char> key1 = new List<char>(map1.Keys);
        List<char> key2 = new List<char>(map2.Keys);

        value1.Sort();
        value2.Sort();
        key1.Sort();
        key2.Sort();

        if (value1.SequenceEqual(value2) && key1.SequenceEqual(key2))
        {
            return true;
        }
        return false;

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