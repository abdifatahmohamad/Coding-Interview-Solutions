public class Solution {
    public IList<string> CommonChars(string[] words)
    {
        Dictionary<char, int> commonChars = CountChars(words[0]);
        for (int i = 1; i < words.Length; i++)
        {
            // Get character counts for the current word
            Dictionary<char, int> currentWordChars = CountChars(words[i]);

            // Update the common characters dictionary
            foreach (var key in new List<char>(commonChars.Keys))
            {
                if (currentWordChars.ContainsKey(key))
                {
                    commonChars[key] = Math.Min(commonChars[key], currentWordChars[key]);
                }
                else
                {
                    commonChars.Remove(key);
                }
            }
        }

        // Convert the common characters dictionary to a list of strings
        List<string> res = new List<string>();
        foreach (var pair in commonChars)
        {
            for (int i = 0; i < pair.Value; i++)
            {
                res.Add(pair.Key.ToString());
            }
        }

        return res;
    }

    private Dictionary<char, int> CountChars(string word)
    {
        Dictionary<char, int> charCounts = new Dictionary<char, int>();
        foreach (var c in word)
        {
            if (charCounts.ContainsKey(c))
            {
                charCounts[c]++;
            }
            else
            {
                charCounts[c] = 1;
            }
        }
        return charCounts;
    }
}