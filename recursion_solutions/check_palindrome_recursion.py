# Reference: vhttps://www.youtube.com/watch?v=twuC1F6gLI8&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=4

# Write a function that checks if string is a palindrome or not (True or False)
# Time complexity is N / 2 (half on N) || Space is O(N)
def isPalindrome(i, s):
    if i >= len(s) // 2:
        return True
    if s[i] != s[len(s) - i -1]:
        return False
    return isPalindrome(i + 1, s)


if __name__ == "__main__":
    s = "madam"
    print(isPalindrome(0, s))