def missing_char(word, ch):
    new_list = []
    for i in range(len(word)):
        if word[i] != ch:
            new_list.append(word[i])
    return "".join(new_list)


print(missing_char("somalia", "a"))


# Solving this problem using bucket
def missing_chars(word: str, target: str) -> str:
    # If target char is NOT present in the word
    if target not in word:
        return "Not found!"

    word = word.lower()
    missing = [False] * 26
    for char in word:
        if char == target:
            i = ord(char) - ord("a")
            missing[i] = True

    res = []
    for ch in word:
        i = ord(ch) - ord("a")
        if missing[i] != True:
            res.append(ch)
    return "".join(res)


print(missing_chars("somalis", "s"))
