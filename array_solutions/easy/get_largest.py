def get_largest(arr):
    largest = float('-inf')
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest


arr = [2, 9, 22, 2, 1]
print(get_largest(arr))
