# Valid Anagram

import re

def valid_anagram(str1, str2):
   # Remove special character to the string:
    str1 = re.sub('[^A-Za-z0-9]+', '', str1).lower()
    str2 = re.sub('[^A-Za-z0-9]+', '', str2).lower()
   # Cast string as a list
    list_str1, list_str2 = list(str1), list(str2)
   # Sort the string	  
    list_str1.sort()
    list_str2.sort()
   # Compare the two string and return a boolean	
    return (list_str1 == list_str2)   

print(valid_anagram('', '')) # True
print(valid_anagram('', '?')) # True
print(valid_anagram('aaz', 'zza')) # False
print(valid_anagram('Anagram', 'nagaram')) # True
print(valid_anagram('rat', 'car')) # False
print(valid_anagram('awesome', 'awesom')) # False
print(valid_anagram('qwerty', 'qeywrt')) # True
print(valid_anagram('texttwisttime', 'timetwisttext')) # True

######################################################################################################
# Write a Python function to check whether a string is pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
# Hint: Look at the string module
# import string --> print(string.ascii_lowercase) 'abcdefghijklmnopqrstuvwxyz'
# print(ispangram("The quick brown fox jumps over the lazy dog")) # output: True
#print(ispangram("This string is missing some letters")) # output: False

import string, re


def ispangram(str1, alphabet=string.ascii_lowercase):
    # Remove special character to the string:
    str1 = re.sub('[^A-Za-z0-9]+', '', str1).lower()
    alphaset = set(alphabet)
    return alphaset <= set(str1)


print(ispangram('The quick brown fox jumps over the lazy dog'))  # output: True
print(ispangram("This string is missing some letters"))  # output: False
####################################################################################################
# Move Zeros:
# arr = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
def move_zeros(arr):
    index = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            temp = arr[index]
            arr[index] = arr[i]
            arr[i] = temp
            index += 1
    return arr

print(move_zeros([0, 1, 0, 3, 12]))

###################################################################################################
'''Write a function called sumZero which accepts a sorted array of integers. 
The function should find the first pair where the sum is 0. 
Return an array that includes both values that sum to s=zero or undefined if a pair does not exist.'''

from typing import List 

def sum_zero(arr: List[int]) -> List[int]:
	left = 0
	right = len(arr)-1
# 	arr.sort() If it's not sorted
	while left < right:
		total = arr[left] + arr[right]
		if total == 0:
			return [arr[left], arr[right]]
		elif total > 0:
			right -= 1
		else:
			left +=1
	return []

arr = [-4, 2, 0, -3, 15, 3, 10, 3, -2]
print(sum_zero(arr))

# O(n) Time
# O(1) Space

#####################################################################################################
# Array Pair Sum: 
'''Given an integer array, output all the unique pairs that sum up to a specific value k.
pair_sum([1,3,2,2], 4) Output: 2 pairs of (1,3), (2,2)'''

from typing import List


def pair_sum(arr, k: List[int]) -> List[int]:
    # Check if the input is less than num of 2:
    if len(arr) < 2:
        return print('Too small')
    # Create two counters to track our array
    seen = set()
    output = set()
    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

    print('\n'.join(map(str, list(output))))


pair_sum([1, 3, 2, 2], 4)

##################################################################################################
# Add each previous number in list
# O(N) Time 
# O(1) Space
from typing import List

def add_previous(nums: List[int]) -> List[int]:
    curr_sum = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        nums[i] = curr_sum

    return nums

nums = [1,2,3,4]
print(add_previous(nums))
# output: [1,3,6,10]

#################################################################################################
# Given two sorted integer arrays arr1 and arr2, merge arr2 into arr1 as one sorted array.
# arr1 = [0, 3, 4, 31], arr2 = [4, 6, 30] # Output: [0, 3, 4, 4, 6, 30, 31]

def mergeSortedArray(arr1, arr2):
    mergedArray = []
    # Grab the length of arr1:
    len1 = len(arr1)
    # Grab the length of arr2:
    len2 = len(arr2)
    # Index of arr1
    i = 0
    # Index of arr2
    j = 0

    # check the input:
    if len1 == 0:
        return arr2
    if len2 == 0:
        return arr1

    # While loop to check til i and j within the length of both arr1 and arr2:
    while ((i < len1) and (j < len2)):
	# Check which array is smaller and push it to the empty array:
        if arr1[i] < arr2[j]:
            mergedArray.append(arr1[i])
            i += 1
        else:
            mergedArray.append(arr2[j])
            j += 1
    while i < len1:
        mergedArray.append(arr1[i])
        i += 1
    while j < len2:
        mergedArray.append(arr2[j])
        j += 1

    return mergedArray


print(mergeSortedArray([0, 3, 4, 31], [4, 6, 30]))

