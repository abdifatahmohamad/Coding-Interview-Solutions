# O(N LOG N) Time || O(1) Space
def find_smallest_interval(num):
    num.sort()
    smallest = num[1] - num[0]
    for i in range(1, len(num) - 1):
        diff = num[i + 1] - num[i]
        if diff < smallest:
            smallest = diff
    return smallest


num1 = [1, 6, 4, 8, 2]
num2 = [6, 4, 8, 2]
print(find_smallest_interval(num2))
