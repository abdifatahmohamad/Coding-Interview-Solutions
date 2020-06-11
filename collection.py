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

#####################################################################################################
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

####################################################################################################
'''Write a function called sumZero which accepts a sorted array of integers. 
The function should find the first pair where the sum is 0. 
Return an array that includes both values that sum to s=zero or undefined if a pair does not exist.'''

from typing import List 

def sum_zero(arr: List[int]) -> List[int]:
	left = 0
	right = len(arr)-1
	arr.sort()
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
print(sum_zeros(arr))

#####################################################################################################




