class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = {}
        for c in s:
            frequency[c] = frequency.get(c, 0) + 1

        heap = []
        for n in frequency:
            heap.append((frequency.get(n), n))

        heap.sort(key=lambda x: (-x[0], x[1]))

        res = []
        for c in heap:
            res.append((c[1] * c[0]))
        return "".join(res)
        