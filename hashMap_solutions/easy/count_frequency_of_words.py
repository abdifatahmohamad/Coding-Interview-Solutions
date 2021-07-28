string = input("Enter String: ")
splitString = string.split()
empty_dict = {}
for char in splitString:

    # if char not in empty_dict.keys():
    #     empty_dict[char] = 0
    # empty_dict[char] = empty_dict[char] + 1

    # The same above code but easier
    # if char in empty_dict:
    #     empty_dict[char] += 1
    # else:
    #     empty_dict[char] = 1

    # The same above code but shorter
    empty_dict[char] = empty_dict.get(char, 0) + 1
print(empty_dict)
