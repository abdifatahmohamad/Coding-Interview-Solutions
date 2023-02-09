class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
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
    for word, frequency in mapping.items():
        if frequency > max_freq or (frequency == max_freq and word < max_word):
            max_freq = frequency
            max_word = word
    return max_word
        