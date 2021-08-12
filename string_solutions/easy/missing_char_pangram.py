
class Solution:
    def missing_char_pangram(self, s: str) -> str:
        present = [False] * 26
        for i in range(len(s)):
            if 'a' <= s[i] <= 'z':  # s[i] >= 'a' and s[i] <= 'z':
                present[ord(s[i]) - ord('a')] = True
            elif 'A' <= s[i] <= 'Z':  # s[i] >= 'A' and s[i] <= 'Z':
                present[ord(s[i]) - ord('A')] = True

        res = []

        for i in range(26):
            if not present[i]:  # present[i] == False:
                # Increment while appending the letters in the list
                res.append(chr(ord('a') + i))

        return "".join(res)

    # Another way
    def missing_char_pangram(s: str) -> str:
        s = s.lower()
        missing = [False] * 26
        # for i in range(len(s)):
        for ch in s:

            # if 'a' <= s[i] <= 'z':
            # missing[ord(s[i]) - ord('a')] = True

            if ch.isalpha():
                missing[ord(ch) - ord('a')] = True

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        res = []
        # Check if char is missing from our previous string
        for i in range(len(missing)):
            if missing[i] == False:
                res.append(alphabet[i])
        return "".join(res)


print(missing_char_pangram("The quick brown fox jumps"))

solution = Solution()
print(solution.missing_char_pangram("The quick brown fox jumps"))  # adglvyz
print(solution.missing_char_pangram(
    "The quick brown fox jumps over the lazy dog"))  # ""
