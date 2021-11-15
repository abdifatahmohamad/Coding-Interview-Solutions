def compressWords(string):
    res = []
    count = 1
    i = 1
    while i < len(string):
        if string[i] == string[i - 1]:
            count += 1
            i += 1
            continue
        if count > 1:
            res.append(string[i - 1])
            res.append(str(count))
            count = 1
        else:
            res.append(string[i - 1])
        i += 1

    if count > 1:
        res.append(string[i - 1])
        res.append(str(count))
    else:
        res.append(string[i - 1])

    return "".join(res)


string0 = "abaabbbc"  # ===> aba2b3c
string1 = "ab"  # ===> "ab"
string2 = "aa"  # ===> "ab"
string3 = "abb"  # ===> "ab2"
print(compressWords(string0))


##########################
# Similar solution:
def compressWords(message):
    compressed = []
    count = 1
    for i in range(len(message) - 1):
        if message[i] == message[i + 1]:
            count += 1
        else:
            compressed.append(message[i])
            if count != 1:
                compressed.append(str(count))
            count = 1
    compressed.append(message[i])
    if count > 1:
        compressed.append(str(count))
    return "".join(compressed)


msg0 = "abaabbbc"  # ===> aba2b3c
msg1 = "ab"  # ===> "ab"
msg2 = "aa"  # ===> "a2"
msg3 = "abb"  # ===> "ab2"
print(compressWords(msg0))
