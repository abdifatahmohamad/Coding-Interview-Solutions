# O(N) Time || O(1) Space
def find_smallest_interval(arr):
    first = second = float('inf')
    for num in arr:
        if num < first:
            second = first
            first = num
        elif num < second and num != first:
            second = num

    return [first, second]


num1 = [1, 6, 4, 8, 2]
num2 = [6, 4, 8, 2]
print(find_smallest_interval(num2))
