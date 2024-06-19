# Reference: https://www.youtube.com/watch?v=twuC1F6gLI8&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=4

# Reverse array recursively
# def reverse_array(arr, l, r):
#     if l >= r:
#         return
#     swap(arr, l, r)
#     reverse_array(arr, l + 1, r - 1)

# # Helper function to swap array
# def swap(arr, l, r):
#     arr[l], arr[r] = arr[r], arr[l]

# if __name__ == "__main__":
#     arr = [1, 3, 2, 5, 4]
#     l, r = 0, len(arr) - 1
#     reverse_array(arr, l, r)
#     print(arr)

# Reverse array in a single i:
# Time complexity is N / 2 (half on N) || Space is O(N)
def reverse_array(i, arr, n):
    if i >= n // 2:
        return
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    # With helper function
    # swap(arr, i, n - i - 1)
    reverse_array(i + 1, arr, n)

# Helper function to swap array
# def swap(arr, l, r):
#     arr[l], arr[r] = arr[r], arr[l]
    

if __name__ == "__main__":
    arr = [1, 3, 2, 5, 4]
    n = len(arr)
    reverse_array(0, arr, n)
    print(arr)

