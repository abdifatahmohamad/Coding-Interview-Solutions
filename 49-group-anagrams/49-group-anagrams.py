class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for word in strs:
            alpha = [0 for _ in range(26)]
            for c in word:
                alpha[ord(c) - ord('a')] += 1
                
            key = tuple(alpha)
            if key not in mapping:
                mapping[key] = []
            mapping[key].append(word)
            
        return mapping.values()