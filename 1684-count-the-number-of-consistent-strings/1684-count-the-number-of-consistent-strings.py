class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        '''
            allowed = "ab"
            words = ["ad", "bd", "aaab", "baa", "badab"]
            
            map = {
                "a": 1
                "b": 1
            }
        
        '''
        
        allowed_set = set(allowed)
        res = 0
        for word in words:
            valid = True
            for char in word:
                if char not in allowed_set:
                    valid = False
                    break
            if valid:
                res += 1
        return res

        
        
        
        
        