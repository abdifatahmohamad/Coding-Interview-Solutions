class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {c: i for i, c in enumerate(order)}
        
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            for j in range(len(word1)):
                # if word2 is brefix of word1, return False
                if j == len(word2):
                    return False
                
                # Look for first different character
                word1Char, word2Char = word1[j], word2[j]
                if word1Char != word2Char:
                    # Verify that character in word1 comes before character in word2
                    # in our order in mapping dictionary
                    # If character in word2 suppose to be greater than word1
                    if mapping.get(word1Char) > mapping.get(word2Char):
                        return False
                    # Character in word1 suppose to be greater than word2
                    # stop comparing the two words, we found the first different character
                    break
                    
        return True
        