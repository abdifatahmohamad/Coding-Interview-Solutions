class Solution:
    def minDeletionSize(self, s: List[str]) -> int:
        res = []
        for i in range(len(s[0])):
            new_string = ""
            for j in range(len(s)):
                new_string += s[j][i]
            res.append(new_string)

        # res give us ['abc', 'bca', 'cee'], ['cdg', 'bah', 'afi']

        min_deletions = 0
        for word in res:
            for i in range(len(word) - 1):
                if ord(word[i + 1]) < ord(word[i]):
                    min_deletions += 1
                    break
        return min_deletions
        