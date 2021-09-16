# Brute force solution using auxiliary data structure O(N) ST
def adjacentElementsProduct(nums):
    res = []
    n = len(nums)
    for i in range(n - 1):
        res.append(nums[i] * nums[i + 1])
    return res

    # One line return using list comprehension:
    # return max([nums[i] * nums[i+1] for i in range(len(nums)-1)])

# Optimized solution O(N) Time || O(1) Space


def adjacentElementsProduct(nums):
    res = float('-inf')
    n = len(nums)
    for i in range(n - 1):
        result = nums[i] * nums[i + 1]
        if res < result:
            res = result
    return res


nums = [3, 6, -2, -5, 7, 3]
# The output should be (7 * 3) = 21
print(adjacentElementsProduct(nums))
