def frequencySort(s):
    frequency = {}
    for c in s:
        frequency[c] = frequency.get(c, 0) + 1

    heap = []
    for n in frequency:
        heap.append((frequency.get(n), n))

    # Sort it in decreasing order based on the frequency of the characters
    heap.sort(key=lambda x: (-x[0], x[1]))  # [(2, 'e'), (1, 'r'), (1, 't')]

    res = []
    for i, c in heap:
        res.append((c * i))
    return "".join(res)


print(frequencySort("tree"))  # Output: eert
# print(frequencySort("cccaaa")) # Output: aaaccc
