# Write a function that checks if string is a palindrome or not (True or False)

def isPalindrome(i, s):
    if i >= len(s) // 2:
        return True
    if s[i] != s[len(s) - i -1]:
        return False
    return isPalindrome(i + 1, s)


if __name__ == "__main__":
    s = "madam"
    print(isPalindrome(0, s))