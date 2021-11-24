# O(N) Time || O(1) Space
def find_smallest_interval(arr):
    first = second = float('inf')
    for num in arr:
        if num < first:
            second = first
            first = num
        elif num < second and num != first:
            second = num

    return abs(first - second)


# O(N LOG N) Time || O(1) Space
def find_smallest_interval(num):
    num.sort()
    smallest = num[1] - num[0]
    for i in range(1, len(num) - 1):
        diff = num[i + 1] - num[i]
        if diff < smallest:
            smallest = diff
    return smallest


# O(N^2) Time || O(1) Space
def find_smallest_interval(num):
    smallest = float('inf')
    for i in range(len(num) - 1):
        for j in range(i + 1, len(num)):
            if abs(num[i] - num[j]) < smallest:
                smallest = abs(num[i] - num[j])
    return smallest


num1 = [1, 6, 4, 8, 2]
num2 = [6, 4, 8, 2]
print(find_smallest_interval(num2))
