class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        window = defaultdict(int)
        for i, c in enumerate(s2):
            window[c] += 1
            if i >= len(s1):
                left = s2[i - len(s1)]
                if window[left] == 1:
                    del window[left]
                else:
                    window[left] -= 1
            if s1_counter == window:
                return True
        return False
        
        