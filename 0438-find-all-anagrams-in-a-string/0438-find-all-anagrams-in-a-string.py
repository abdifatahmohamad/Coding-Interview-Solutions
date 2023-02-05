class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        mapping = defaultdict(int)
        for c in p:
            mapping[c] += 1
        counter = len(mapping)
        left, right = 0, 0
        while right < len(s):
            c = s[right]
            if c in mapping:
                mapping[c] -= 1
                if mapping[c] == 0:
                    counter -= 1
            right += 1
            while counter == 0:
                temp = s[left]
                if temp in mapping:
                    mapping[temp] += 1
                    if mapping[temp] > 0:
                        counter += 1
                if right - left == len(p):
                    res.append(left)
                left += 1
        return res
        