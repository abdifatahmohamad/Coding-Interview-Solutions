def missing_chars(word: str, target: str) -> str:
    # If target char is NOT present in the word
    if target not in word:
        return "Not fount!"

    mapping = {}
    for char in word:
        mapping[char] = mapping.get(char, 0) + 1

    for ch in word:
        if ch == target:
            mapping[ch] -= 1
        if mapping[ch] == 0:
            del mapping[ch]
    return "".join(mapping.keys())


###################################################################
def missing_chars(word: str, target: str) -> str:
    # If target char is NOT present in the word
    if target not in word:
        return "Not fount!"

    mapping = {}
    for char in word:
        mapping[char] = mapping.get(char, 0) + 1

    for ch in word:
        if target in mapping:
            del mapping[ch]
    return "".join(mapping.keys())


################################ Without using DEL ######################################
def missing_chars(word: str, target: str) -> str:
    # If target char is NOT present in the word
    if target not in word:
        return "Not fount!"

    mapping = {}
    for char in word:
        mapping[char] = mapping.get(char, 0) + 1

    res = []
    for ch in word:
        if ch == target:
            mapping[ch] -= 1
        else:
            res.append(ch)
    return "".join(res)


#################################################################
def missing_chars(word: str, target: str) -> str:
    # If target char is NOT present in the word
    if target not in word:
        return "Not fount!"

    mapping = {}
    for char in word:
        mapping[char] = mapping.get(char, 0) + 1

    res = []
    for ch in word:
        if ch == target:
            mapping[ch] -= 1

    for ch in word:
        if mapping[ch] > 0:
            res.append(ch)
    return "".join(res)


print(missing_chars("somalis", "s"))  # -> omali
