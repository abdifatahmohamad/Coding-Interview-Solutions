import re


# O(N) Time || O(N) Space
def camel_case() -> str:
    # Take user's input
    string = input("Enter a sentence: ")
    # Strip away non alphanumeric characters from the string
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


###################################################
string = input("Enter a sentence: ")  # hi there, my name is abdifatah!
sen = re.sub('[^A-Za-z0-9]+', ' ', string)
sen = sen.split()

res = []
for i in range(len(sen)):
    first = sen[i][0].upper()
    rest = sen[i][1:]
    camelCase = first + rest
    res.append(camelCase)
print("".join(res))

##########################################
string = input("Enter a sentence: ")  # hi there, my name is abdifatah!
sen = re.sub('[^A-Za-z0-9]+', ' ', string)
sen = sen.split()

# res = ""
# for word in sen:
#     res += word[0].upper() + word[1:]
# print("".join(res))

# Same above code using string comprehension
res = "".join(word[0].upper() + word[1:] for word in sen)
print(res)

###################################################

string = input("Enter a sentence: ")  # hi there, my name is abdifatah!
sen = re.sub('[^A-Za-z0-9]+', ' ', string)
sen = sen.split()

# res = []
# for word in sen:
#     res.append(word[0].upper() + word[1:])
# print("".join(res))

# Same above code using list comprehension
res = "".join([word[0].upper() + word[1:] for word in sen])
print(res)

# hi there, my name is abdifatah!
print(camel_case())  # HiThereMyNameIsAbdifatah
