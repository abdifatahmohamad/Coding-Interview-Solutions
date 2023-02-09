def topKFrequent(words, k):
    mapping = {}
    for c in words:
        mapping[c] = mapping.get(c, 0) + 1

    # Find top k elements
    result = []
    for i in range(k):
        max_word = find_top_word(mapping)
        result.append(max_word)
        del mapping[max_word]

    return result


# Find top word from the dictionary
def find_top_word(mapping):
    max_freq = 0
    max_word = ""
    for word, freq in mapping.items():
        if freq > max_freq or (freq == max_freq and word < max_word):
            max_freq = freq
            max_word = word
    return max_word


print(topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
print(topKFrequent(["the", "day", "is", "sunny",
                    "the", "the", "the", "sunny", "is", "is"], 4))
