class Solution:
    def customSortString(self, order: str, s: str) -> str:
        mp = {}
        for c in s:
            mp[c] = mp.get(c, 0) + 1

        # res = [0 for _ in range(len(order))] 
        # res = [0] * len(order)
        res = []
        # order_index = {ch: i for i, ch in enumerate(order)}
        for ch in order:
            if ch in mp:
                # index = order_index[ch]
                # res[index] = ch * mp[ch]
                res.append(ch * mp[ch])
                del mp[ch]

        for ch, freq in mp.items():
            res.append(ch * freq)
        # resStr = str(res)

        return "".join(res)
        