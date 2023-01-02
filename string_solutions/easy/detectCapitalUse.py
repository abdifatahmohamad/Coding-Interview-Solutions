def detectCapitalUse(word):
    return is_all_letters_capital(word) or \
        is_all_letters_lower(word) or \
        is_title_case(word)


# Handle all letters capital
def is_all_letters_capital(word):
    for c in word:
        if c.islower():
            return False
    return True


# Handle all letters lower
def is_all_letters_lower(word):
    for c in word:
        if c.isupper():
            return False
    return True


# Handle first letter capital
def is_title_case(word):
    # Returns whether the first letter is upper or lower (true or false)
    isFirstUpper = word[0].isupper()
    isRestLower = True
    for i in range(1, len(word)):
        if word[i].isupper():
            isRestLower = False

    return isFirstUpper and isRestLower


print(detectCapitalUse("USA"))
print(detectCapitalUse("leetcode"))
print(detectCapitalUse("Google"))
print(detectCapitalUse("FlaG"))
