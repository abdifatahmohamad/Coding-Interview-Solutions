class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        '''
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        mapping = {}
        for char in sentence:
            mapping[char] = True
        
        return len(mapping) == len(alphabet)
        
        '''
        # Set solution:
        '''
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        found = set()
        for char in sentence:
            found.add(char)
        
        return len(found) == len(alphabet)
        '''
        
        # Bucket solution:
        bucket = [0 for _ in range(26)]
        for c in sentence:
            # if 'a' <= c <= 'z':
            if 'a' <= c or 'z' <= c:
                bucket[ord(c) - ord('a')] = True
        
        for ch in bucket:
            if not ch:
                return False
        
        return True  
            
        
        