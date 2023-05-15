class Solution:
    def customSortString(self, order: str, s: str) -> str:
        mp = {}
        for c in s:
            mp[c] = mp.get(c, 0) + 1

        res = []
        for ch in order:
            if ch in mp:
                res.append(ch * mp[ch])
                del mp[ch]

        for ch, freq in mp.items():
            res.append(ch * freq)
            
        return "".join(res)
        