def sortPeople(names, heights):
    mapping = {}
    for i in range(len(names)):
        mapping[heights[i]] = names[i]

    # Sort dictionary
    # mapping = sorted(mapping.items(), reverse=True)
    # res = []
    # for _, people in mapping:
    #     res.append(people)
    # return res

    # Another approach
    heights = sorted(heights, reverse=True)
    res = []
    for height in heights:
        res.append(mapping.get(height))
    return res


print(sortPeople(["Mary", "John", "Emma"], [180, 165, 170]))
# ["Mary","Emma","John"]
print(sortPeople(["Alice", "Bob", "Bob"], [155, 185, 150]))
# ["Bob","Alice","Bob"]
