# https://edabit.com/challenge/yPsS82tug9a8CoLaP

def character_mapping(txt):
    d = {}
    res = []
    counter = 0
    for char in txt:
        if char not in d:
            d[char] = counter
            res.append(d[char])
            counter += 1
        else:
            d[char] = d.get(char)
            res.append(d[char])

    return res


# Neater solution
def character_mapping(seq):
    dic = {}
    counter = 0
    for char in seq:
        if char in dic:
            continue
        dic[char] = counter
        counter += 1

    # res = []
    # for char in seq:
    #     res.append(dic[char])
    # return res

    # Shorter version
    return [dic[char] for char in seq]


print(character_mapping("babbcb"))  # ➞ [0, 1, 0, 0, 2, 0]
# print(character_mapping("hmmmmm")) # ➞ [0, 1, 1, 1, 1, 1]
