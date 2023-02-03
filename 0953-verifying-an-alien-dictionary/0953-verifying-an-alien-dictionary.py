class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {n: i for i, n in enumerate(order)}

        for i in range(1, len(words)):
            prevWord, currWord = words[i - 1], words[i]
            for j in range(len(prevWord)):
                if j == len(currWord):
                    return False

                prevChar, currChar = prevWord[j], currWord[j]
                if prevChar != currChar:
                    if mapping.get(prevChar) > mapping.get(currChar):
                        return False
                    break

        return True
        