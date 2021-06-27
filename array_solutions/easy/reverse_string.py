# Reverse String using two pointers
def revString(s):
    arr = list(s)
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return "".join(arr)


print(revString("Hello"))
