def find_length(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i]:
            count += 1
        else:
            break
    return count


arr = [1, 2, 4, 1, 3, 3, 2, 9, 2, 1, 9, 7, 7]
print(find_length(arr))
