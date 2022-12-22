from collections import Counter


# Different ways to get keys and values from dictionary
def dictionary(s):
    mapping = Counter(s)
    for d in mapping:
        print("Keys: ", d)
        print("Values: ", mapping[d])

    for k in mapping.keys():
        print("Keys: ", k)

    for v in mapping.values():
        print("Values: ", v)

    for k, v in mapping.items():
        print("Keys: ", k)
        print("Values: ", v)

    return mapping


print(dictionary("abcabcbb"))
