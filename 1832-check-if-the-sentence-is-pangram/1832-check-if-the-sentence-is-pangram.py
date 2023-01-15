class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        mapping = {}
        for char in sentence:
            mapping[char] = True
        
        return len(mapping) == len(alphabet)
            
            
        
        