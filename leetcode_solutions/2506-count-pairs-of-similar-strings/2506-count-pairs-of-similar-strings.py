class Solution:
    def similarPairs(self, words: List[str]) -> int:
        # Sort each string in the list
        sorted_words = []
        for word in words:
            sorted_words.append(''.join(sorted(word)))

        # Remove duplicates from each string in the list
        unique_words = []
        for word in sorted_words:
            unique_words.append(set(word))

        # Count the number of string pairs the have similar string
        count = 0
        for i in range(len(unique_words)):
            for j in range(i + 1, len(unique_words)):
                if unique_words[i] == unique_words[j]:
                    count += 1
        return count
        