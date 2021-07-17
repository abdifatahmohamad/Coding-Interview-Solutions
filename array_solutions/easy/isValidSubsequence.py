# O(n) time | O(1) space --> where n is the length of the array
def isValidSubsequence(array, sequence):
	count = index = 0
    for curr in array:
        if count != len(sequence) and curr == sequence[index]:
            count += 1
            index += 1
    return count == len(sequence)

# Another way to solve it using for while loop:
def isValidSubsequence(array, sequence):
	arrIdx = 0
    seqIdx = 0
    while (arrIdx < len(array)) and (seqIdx < len(sequence)):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(isValidSubsequence(array, sequence))
# Output: True
