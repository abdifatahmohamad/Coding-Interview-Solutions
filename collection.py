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

####################################################################################################
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
# reverse list of numbers: num = [1,2,3,4,5,6,7,8,9], Output: [9, 8, 7, 6, 5, 4, 3, 2, 1]

def rev_list(num):
  # Grab the length of our list:
    length = len(num)

    # Using for loop through starting zero til length divided by 2 index
    # Swapping 2 indexing:
    for i in range(length//2):
      num[i], num[length - i - 1] = num[length - i - 1], num[i]

    print(num)

num = [1,2,3,4,5,6,7,8,9]
rev_list(num)

###################################################################################################
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

###################################################################################################
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

#################################################################################################
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


print(mergeSortedArray([0, 3, 4, 31], [4, 6, 30])) # Output: [0, 3, 4, 4, 6, 30, 31]

#################################################################################################
# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# Note: You are not suppose to use the library's sort function for this problem.

def sortArray(nums):
    start, current, end = 0, 0, len(nums)-1

    while current <= end:
        if nums[current] == 0:
            swap(nums, current, start)
            current += 1
            start += 1
        elif nums[current] == 2:
            swap(nums, current, end)
            end -= 1
        else:
            current += 1
    return nums


def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


nums1 = [2,0,2,1,1,0]
# Output = [0,0,1,1,2,2]
# You can't use sort built-in methods
print(sortArray(nums1))

#################################################################################################
# Create a function that asks the user how many Fibonacci numbers to generate and then generates them:

def fibonacci():
    num = int(input("Please enter how many numbers you want in this series :"))
    first = 0
    second = 1
    if num == 0 or num == 1:
        print(f'Please enter a number that is more than {num}')
    else:
        for number in range(num):
            print(first, end=' ')
            # Swap/Shift numbers in the list:
            temp = first + second
            first = second
            second = temp + second


fibonacci()

################################################################################################
class Solution(object):
    def fib(self, N: int) -> int:
        first, second = 0, 1
        if N < 0:
            print('Incorrect Input')
        elif N == 1:
            return first
        elif N == 1:
            return second
        else:
            for i in range(2, N + 1):
                temp = first + second
                first = second
                second = temp
            return second

N = 10
solution = Solution()
print(solution.fib(N))
###################################################################################################
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.
# s = "A man, a plan, a canal: Panama" # Output: True
# s = "race a car" # Output: False

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove special character to the string:
        s = re.sub('[^A-Za-z0-9]+', '', s).lower()
        rev_str = s[::-1]

        if s == rev_str:
            return True
        else:
            return False

s = "A man, a plan, a canal: Panama" # Output: True
# s = "race a car" # Output: False
solution = Solution()
print(solution.isPalindrome(s))

#################################################################################################
# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].
# Input: nums = [1,2,3,4,4,3,2,1], n = 4
# Output: [1,4,2,3,3,2,4,1]

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[n + i])

        return result


nums = [2, 5, 1, 3, 4, 7]
n = 3
solution = Solution()
print(solution.shuffle(nums, n))

###################################################################################################
# The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].
# If a[i] > b[i], then Alice is awarded 1 point.
# If a[i] , then Bob is awarded 1 point.
# If a[i] = b[i], then neither person receives a point.
# Comparison points is the total points a person earned.
# Given a and b, determine their respective comparison points.

def compare_triplets(a,b):
    alice = 0
    bob = 0

    for i in range(0, len(a)):
        if a[i] > b[i]:
            alice += 1
        if a[i] < b[i]:
            bob += 1
    return [alice, bob]

# a = [1, 2, 3]
# b = [3, 2, 1]
# a = [17, 28, 30]
# b = [99, 16, 8]
a = [17, 28, 30]
b = [17, 28, 30]
print(compare_triplets(a, b))

###################################################################################################
# Google question:
# Given a bunch of characters, create a function that returns the first recurrent character:
# first_recurring('DBCBA') # Output: 'B'
# first_recurring('DACBAB') # Output: 'A'
# first_recurring('ABC') # Output: None

def first_recurring(given_string):

    character = given_string.lower()

    seen = {}

    for char in character:
        if char in seen:
            return char
        else:
            seen[char] = 1
    # After the above loop is done, that means there no recurrent character so return None:
    return None

print(first_recurring('ABCDAB')) #Output: a

###################################################################################################



