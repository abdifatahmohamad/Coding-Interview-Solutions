# Reference: https://www.youtube.com/watch?v=kvRjNm4rVBE&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=5
# A subsequence is a contiguous or non-contiguous sequences which follows the order of the array
def print_subsequences(i, subsequence, arr, n):
    n = len(arr)
    # Base case
    if(i >= n):
        print([n for n in subsequence])
        return
    # Not pick or take condition, this element isn't added into your subsequence
    print_subsequences(i + 1, subsequence, arr, n) # If you want to reverse; put this code back
    # Take or pick the particular index into the subsequence
    subsequence.append(arr[i])
    print_subsequences(i + 1, subsequence, arr, n) # Take the index
    subsequence.pop()
    
if __name__ == "__main__":
    arr = [3, 1, 2]
    n = len(arr)
    subsequence = []
    print_subsequences(0, subsequence, arr, n)

'''
All the subsequences of arr = [3, 1, 2]
{}
3
1
2
3, 1
1, 2
3, 2
3, 1, 2
'''
# Sub array can be subsequence 
"""
3, 2, 1 isn't subsequence array because isn't following the order of the array
"""

