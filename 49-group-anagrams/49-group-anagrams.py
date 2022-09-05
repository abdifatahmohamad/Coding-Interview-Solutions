class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for word in strs:
            alpha = [0 for _ in range(26)]
            for c in word:
                alpha[ord(c) - ord('a')] += 1
                
            key = tuple(alpha)
            mapping[key].append(word)
            
        return mapping.values()