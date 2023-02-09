class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mapping = Counter(words)
        res = []
        for i in range(k):
            max_frequency = 0
            max_word = ""
            for word, frequency in mapping.items():
                if frequency > max_frequency or (frequency == max_frequency and word < max_word):
                    max_frequency = frequency
                    max_word = word
            res.append(max_word)
            del mapping[max_word]

        return res
        