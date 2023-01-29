def sortPeople(names, heights):
    mapping = {}
    for i in range(len(names)):
        mapping[heights[i]] = names[i]

    mapping = sorted(mapping.items(), reverse=True)
    res = []
    for _, people in mapping:
        res.append(people)
    return res


# ["Mary","Emma","John"]
print(sortPeople(["Mary", "John", "Emma"], [180, 165, 170]))
# ["Bob","Alice","Bob"]
print(sortPeople(["Alice", "Bob", "Bob"], [155, 185, 150]))
