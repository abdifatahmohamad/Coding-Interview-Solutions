

class Solution:
    def missing_char_pangram(self, string: str) -> str:
        # Python3 program to find characters
        # that needs to be added to make Pangram
        MAX_CHAR = 26
        # A boolean array to store characters
        # present in string.
        present = [False for i in range(MAX_CHAR)]

        # Traverse string and mark characters
        # present in string.
        for i in range(len(string)):
            if (string[i] >= 'a' and string[i] <= 'z'):
                present[ord(string[i]) - ord('a')] = True
            elif (string[i] >= 'A' and string[i] <= 'Z'):
                present[ord(string[i]) - ord('A')] = True

        # Store missing characters in alphabetic
        # order.
        res = ""

        for i in range(MAX_CHAR):
            if (present[i] == False):
                res += chr(i + ord('a'))

        return res


solution = Solution()
print(solution.missing_char_pangram("The quick brown fox jumps"))  # adglvyz
print(solution.missing_char_pangram(
    "The quick brown fox jumps over the lazy dog"))  # ""
