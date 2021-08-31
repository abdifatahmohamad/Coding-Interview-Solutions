# O(N) Time || O(N) Space
def camel_case() -> str:
    # Take user's input
    string = input("Enter a sentence: ")
    # Remove non alphanumeric characters from the string
    sen = re.sub('[^A-Za-z0-9]+', ' ', string)
    # Turn string into a list
    sen = list(sen)
    # An empty list
    res = []
    # Hold first character as an uppercase initially
    res.append(sen[0].upper())
    # Loop through the list starting for first character upto len-1
    for i in range(1, len(sen) - 1):
        curr = sen[i]
        prev = sen[i - 1]
        nxt = sen[i + 1]
        if (curr == ' '):
            # If we encounter an empty space, append next character into the list.
            res.append(nxt.upper())
            # If previous char doesn't have a space, append the current char into the list
        elif (prev != ' '):
            res.append(curr)
    return "".join(res)


# hi there, my name is abdifatah!
print(camel_case())  # HiThereMyNameIsAbdifatah
