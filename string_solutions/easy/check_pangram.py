
class Solution:
    def check_pangram(self, string: str) -> str:
        List = []
        # create list of 26 characters and set false each entry
        for i in range(26):
            List.append(False)

        # converting the sentence to lowercase and iterating
        # over the sentence
        for c in string.lower():
            if not c == " ":
                # make the corresponding entry True
                List[ord(c) - ord('a')] = True

        # check if any character is missing then return False
        for ch in List:
            if ch == False:
                return False
        return True

    # # Driver Program to test above functions
    # string1 = "The quick brown fox jumps over the little lazy dog"
    # # string2 = "This string is missing some letters"
    #
    # if check_pangram(string1):
    #     print('"' + string1 + '"')
    #     print("is a pangram")
    # else:
    #     print('"' + string1 + '"')
    #     print( "is not a pangram")


solution = Solution()
print(solution.check_pangram("This string is missing some letters"))  # False
print(solution.check_pangram("The quick brown fox jumps over the lazy dog"))  # True
