class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        bucket = [0 for _ in range(26)]
        for c in sentence:
            if 'a' <= c <= 'z':
                bucket[ord(c) - ord('a')] = True
        
        for ch in bucket:
            if not ch:
                return False
        
        return True
            
            
        
        