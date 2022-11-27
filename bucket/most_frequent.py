import collections


def most_frequently(data):
    bucket = [0 for _ in range(26)]
    max_val = float("-Inf")
    for c in data:
        # Increment each alphabet location
        index = ord(c) - ord('a')
        bucket[index] += 1

    for val in bucket:
        max_val = max(max_val, bucket[val])

    max_char = ''
    for i, c in enumerate(bucket):
        if max_val == bucket[i]:
            max_char = chr(ord('a') + i)

    return max_char, max_val


# Using bucket sort
def most_frequent(arr):
    count = collections.Counter(arr)
    bucket = [None for _ in range(len(arr) + 1)]
    for ch, freq in count.items():
        bucket[freq] = ch
    for i in range(len(bucket)-1, -1, -1):
        if bucket[i]:
            return bucket[i], i
    return ''


print(most_frequent(['b', 'a', 'a', 'b', 'b',
                     'a', 'c', 'y', 'c', 'b', 'a', 'b']))
print(most_frequent(['z', 'z', 'z', 'z']))
# Add feature to return characters if they have the same fequency
print(most_frequent(['b', 'b', 'a', 'a', 'x', 'x']))
