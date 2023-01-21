class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        mapping = {}
        for ch in allowed:
            mapping[ch] = mapping.get(ch, 0) + 1
            
        res = 0
        for word in words:
            valid = True
            for ch in word:
                if ch not in mapping:
                    valid = False
            if valid:
                res += 1
        return res

        
        
        
        
        