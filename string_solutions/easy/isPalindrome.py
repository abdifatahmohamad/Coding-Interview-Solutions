def isPalindrome(string):
    # res = []
    # for i in range(len(string) - 1, -1, -1):
    #     res.append(string[i])
    # return "".join(res) == string

    # s = list(string)
    # left, right = 0, len(string) - 1
    # while left < right:
    #     s[left], s[right] = s[right], s[left]
    #     left += 1
    #     right -= 1
    # return "".join(s) == string

    # revString = ""
    # for i in range(len(string) - 1, -1, -1):
    #     revString += string[i]
    # return string == revString

    # using slice method
    # s = string[::-1]
    # return s == string

    # Most optimal way O(n) time O(1) space
    left, right = 0, len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


string = "abcdcba"
print(isPalindrome(string))
