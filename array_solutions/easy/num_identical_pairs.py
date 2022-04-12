from collections import defaultdict


def num_identical_pairs(nums):
    dic = {}
    res = 0
    for n in nums:
        if n in dic:
            res += dic[n]
            dic[n] += 1
        else:
            dic[n] = 1
    return res


#####################################################
# Here it is with defaultdict:
def num_identical_pairs(nums):
    dic = defaultdict(int)
    res = 0
    for num in nums:
        res += dic[num]
        dic[num] += 1
    return res


print(num_identical_pairs([1, 2, 3, 1, 1, 3]))  # 4
# print(numIdenticalPairs([1, 1, 1, 1])) # 6
# print(numIdenticalPairs([1, 2, 3]))  # 0
