# Split string into list of characters
'''def split(word):
    return [char for char in word]
##########################################
def split(word):
    # for char in word:
    # splits = []
    # for char in word:
    #     splits.append(char)
    # return splits
#############################################    
    splits = [char for char in word]
    return splits
#############################################    
    # return list(word)
print(split('hello'))'''

##############################################################################
# A program that generates a random number and guesses the right number:
import random

randomNum = random.randint(1, 100)
for _ in range(100):
    guess = int(input('Guess a number'))
    if guess == randomNum:
        print('You got it!')
        break
    elif guess > randomNum:
        print('Your guess is too high')
    else:
        print('Your guess is too low')

# The same program using while loop:

randomNum = random.randint(1, 100)
keep_looping = True
while keep_looping:
    guess = int(input('Guess a number'))
    if guess == randomNum:
        print('You got it!')
        # break
        keep_looping = False
    elif guess > randomNum:
        print('Your guess is too high')
    else:
        print('Your guess is too low')

##############################################################################
#  Use List Comprehension to create a list of the first letters of every word in the string below:
'''st = 'Create a list of the first letters of every word in this string'
my_list = [word[0] for word in st.split()]
print(my_list)'''

# The same above solution using regular for loop:


def makeList(st):
    s = st.split()
    letter = []
    for word in s:
        letter.append(word[0])
    return letter


my_list = 'Create a list of the first letters of every word in this string'
print(makeList(my_list))

####################################################################################
# Program that capitalizes first letter of the string:

# using regular for loop:


def captilizeFirstletter(st):
    # s = st.split()
    # lst = []
    # for word in s:
    #     lst.append(word[0].upper() + word[1:])
    # return ' '.join(lst)

    # using list comprehension
    lst = [word[0].upper() + word[1:] for word in st.split()]
    return ' '.join(lst)

my_list = 'Create a list of the first letters of every word in this string'
print(captilizeFirstletter(my_list))

####################################################################################
'''st = 'Sam Print only the words that start with s in this sentence'
for word in st.split():
    if word[0].lower() == 's':
        print(word)'''
#################################################################################
# Use range() to print all the even numbers from 0 to 10.
'''print(f"The EVEN numbers are:{list(range(0, 11, 2))}")'''
##################################################################################
# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
'''my_list = [num for num in range(1,51) if num % 3 == 0]
print(my_list)'''

# Practice list comprehension:
# Using regular for loop and append:
'''def no_odds(values):
    list = []
    for i in values:
        if i % 2 == 0:
            list.append(i)
    return list
'''
# using regular for loop:


def no_odds(values):
    return [i for i in values if i % 2 == 0]


values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(no_odds(values))

##################################################################################
# Go through the string below and if the length of a word is even print "even!"
'''st = 'Print every word in this sentence that has an even number of letters'

for word in st.split():
  if len(word) % 2 == 0:
    print(f'EVEN strings are: {word}')'''

###############################################################################
# Write a program that prints the integers from 1 to 100. But for multiples of three
# print "Fizz" instead of the number, and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

'''for word in range(1,101):
  if word % 3 == 0 and word % 5 == 0:
    print(f'FizzBuzz')
  elif word % 3 == 0:
    print(f'Fizz')
  elif word % 5 ==0:
    print(f'Buzz')
  else:  
    print(word)'''
##################################################################################
# PIG LATIN problem:
# print(pig_latin(word)) --> ordway
# print(pig_latin(apple)) --> appleay
'''def pig_latin(word):
    first_letter = word[0]
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
        # word[1:] = means word from index one all the way to the end

    return pig_word

print(pig_latin('word'))'''

########################################################################################
# Create function that takes args and returns sum of that args:
'''def myfunc(*args):
    return sum((args))


print(myfunc(1, 2, 3))'''
#########################################################################################
# define a function called myfunc that takes in an arbitrary number of arguments and returns a list

'''def myfunc(*args):
    return [x for x in args if x % 2 == 0]
print(myfunc(1, 2, 3,4,5,6,7,8,9,10)) # [2, 4, 6, 8, 10]'''

###########################################################################################
# Create a function that takes a string and returns a matching string where every even letter is uppercase, and every odd letter is lowercase
# The ouput string can start with either an uppercase or lowercase letter, so long as letters alternate throughout the string.
# myfunc('Anthropomorphism) --> Output: 'aNtHrOpOmOrPhIsM

'''def myfunc(word):
    result = ''
    for index, letter in enumerate(word):
        if index % 2 == 0:
            result += letter.lower()
        else:
            result += letter.upper()
    return result

print(myfunc('Abdifatah'))'''

# The same above code using range loop and append array:


def myfunc(word):
    res = []
    for i in range(len(word)):
        letter = word[i]
        if i % 2 == 0:
            res.append(letter.lower())
        else:
            res.append(letter.upper())
    return ''.join(res)

print(myfunc("abdifatah"))

################################################################################################
# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd¶

'''def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        result = min(a,b)
    else:
        result = max(a,b)
    return result


print(lesser_of_two_evens(13,43))'''
##############################################################################################
# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter¶
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False
'''def animal_crackers(string):
    st1, st2 = string.split()
    return st1[0].upper() == st2[0].upper()


print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))'''

##############################################################################################
# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
# If not, return False¶
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

'''def makes_twenty(n1, n2):
    return (n1 + n2) == 20 or n1 == 20 or n2 == 20

print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))'''

##############################################################################################
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name¶
# old_macdonald('macdonald') --> MacDonald
# Note: 'macdonald'.capitalize() returns 'Macdonald'
'''def capitalize(sentence):
    word = sentence.title()
    return word[:3] + word[3:].capitalize()

print(capitalize('abdifatah'))'''
##############################################################################################
# MASTER YODA: Given a sentence, return a sentence with the words reversed¶
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'
'''def master_yoda(sentence):
    word = sentence.split()
    reverse = word[::-1]
    return ' '.join(reverse)

print(master_yoda('I am home'))
# print(master_yoda('We are ready'))'''
#############################################################################################
# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200¶
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True

'''def almost_there(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10

print(almost_there(210))'''
#############################################################################################
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False
'''def has_33(nums):
    pass

print(has_33([1, 3, 3]))'''
############################
# The same above problem using for loop:

'''def has_33(nums):
    #len(nums)-1 checks the character before last one:
    for i in range(0,len(nums) -1):
        # nums[i] is the number we start chacking and nums[i + 1] is the next number to the prev one
        if nums[i] == 3 and nums[i + 1] == 3:
        # The same above logic using slicing   
        #if nums[i:i + 2] == [3,3]:    
            return True
        return False

print(has_33([1, 3, 3]))'''

##############################################################################################
# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
# The I solved this problem:
'''def paper_doll(string):
    word_list = []
    for char in string:
        word_list.append(char * 3)

    return ''.join(word_list)


print(paper_doll('Hello'))'''
############################################
# An easy way of doing it:
'''def paper_doll(string):
    result = ''
    for char in string:
        result += char * 3

    return result


print(paper_doll('Hello'))'''

##############################################################################################
# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally,
# if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19
'''def blackjack(a, b, c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) - 10 <= 21:
        return sum([a,b,c]) - 10
    else:
        return 'BUST'

# print(blackjack(5,6,7))
print(blackjack(9, 9, 9))
# print(blackjack(9,9,11))'''

###############################################################################################
# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6
# and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14
'''def summer_69(arr):
    while 6 in arr:
        index6 = arr.index(6)
        index9 = arr.index(9)
        del arr[index6:index9 + 1]
    return sum(arr)

# print(summer_69([1, 3, 5]))
# print(summer_69([4, 5, 6, 7, 8, 9]))
# print(summer_69([2, 1, 6, 9, 11]))'''

# Another way of doing it using boolean and while loop:
'''def summer_69(arr):
    total = 0
    #Create a boolean value called add
    add = True

# We gonna use for loop with two nested while loop there and we set it True first:
    for num in arr:
        # while add is equal to True
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        # add is not equal to True(False)
        while not add:
            if num != 9:
                break
            else:
                 add = True
                 break
    return total

# print(summer_69([1, 3, 5]))
# print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))'''

###############################################################################################
# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output :
# No. of Upper case characters : 4
# No. of Lower case Characters : 33
# HINT: Two string methods that might prove useful: .isupper() and .islower()
# If you feel ambitious, explore the Collections module to solve this problem!

'''import re
def up_low(s):
    # s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
    print("A ascii value: ", ord('A'))
    uppercase, lowercase = 0, 0
    for char in s:
        if ord(char) >= 97:
            lowercase += 1
        else:
            uppercase += 1

    print(f'No. of uppercase: {uppercase}')
    print(f'No. of lowercase: {lowercase}')


up_low('Hello Mr. Rogers, how are you this fine Tuesday?')'''

#############################################################################################
# Find the longest word in the string:

def longest_word(string):
    words = string.split(' ')
    longestWord = ''
    for word in words:
        if len(word) > len(longestWord):
            longestWord = word
    return longestWord


print(longest_word('Abdifatah Ali'))  # Output: Abdifatah

#############################################################################################
# Count the number of vowels in a string:


def vowels_count(string):
    count = 0
    vowels = 'aeiou'
    for vowel in string:
        if vowel.lower() in vowels:
            count += 1

    return f'No. of vowels: {count}'


print(vowels_count('Yusuf Abdifatah Ali'))

###############################################################################################
# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
# What if the string is empty? Then the result should be empty object literal, {}.


def count(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


string = 'abca'
print(count(string))

# The same idea but easier:


def count(string):
    counter = {}
    for char in string:
        counter[char] = counter.get(char, 0) + 1
    return counter


string = 'abca'
print(count(string))

##############################################################################################
# Find duplicates from a list of integers and return the result.
# ([3, 4, 4, 3, 6, 3]) # => [4, 6, 3]
# ( https://stackoverflow.com/questions/9835762/how-do-i-find-the-duplicates-in-a-list-and-create-another-list-with-them)

# To compute the list of duplicated elements without libraries:


def remove_duplicates(arr):
    seen = {}
    dupes = []
    for num in arr:
        if num not in seen:
            seen[num] = 1
        else:
            if seen[num] == 1:
                dupes.append(num)
            seen[num] += 1
    return dupes

# This method computes a list of unique elements using set() library:


def remove_duplicates(arr):
    seen = set()
    dupes = []
    for num in arr:
        if num not in seen:
            dupes.append(num)
            seen.add(num)
    return dupes

# The same above code using list comprehension:


def remove_duplicates(arr):
    seen = set()
    return [num for num in arr if num not in seen and not seen.add(num)]


arr = [3, 4, 4, 3, 6, 3]
# Output: [4, 6, 3]
print(remove_duplicates(arr))
##############################################################################################
# Remove the left-most duplicates from a list of integers and return the result.
# Remove the 3's at indices 0 and 3 followed by removing a 4 at index 1
# Input: [3, 4, 4, 3, 6, 3] # => [4, 6, 3], Input: [1,2,1,2,1,2,3] Output:[1,2,3]


def remove_duplicates(arr):
    dupes = []
    array = arr[::-1]
    for num in array:
        if num not in dupes:
            dupes.append(num)
    return dupes[::-1]


arr = [1, 2, 1, 2, 1, 2, 3]
# Output: [1, 2, 3]
print(remove_duplicates(arr))

# The same above solution but different way:


def remove_duplicates(arr):
    result = []
    for index, array in enumerate(arr):
        if array not in arr[index + 1:]:
            result.append(index)
    return result

# Using list comprehension:


def remove_duplicates(arr):
    result = [array for index, array in enumerate(
        arr) if array not in arr[index + 1:]]
    return result

   # Online return:
   # return [array for index, array in enumerate(arr) if array not in arr[index + 1:]]

#############################################################################################

# Find the common numbers in the array list:
# arr1 = [1,2,3,4,6], arr2 = [2,4,6,8] --> Output: [2,4,6]

# Brute-Force Solution:


def solve(arr1, arr2):
    result = []
    d = {}
    for i in arr1:
        d[i] = 1
    for key in arr2:
        if key in d:
            result.append(key)
    return result

# Better Solution:


def find_common_list(arr1, arr2):
    '''

    result = []
    for i in arr1:
        if i in arr2:
            result.append(i)
    return result

    '''
    # One line return:
    return [i for i in arr1 if i in arr2]
    '''result = [i for i in arr1 if i in arr2]
    return result'''

# another better solution using two pointers:


def solve(arr1, arr2):
    i = j = 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            result.append(arr2[j])
            j += 1
        i += 1
    return result


arr1 = [1, 2, 3, 4, 6]
arr2 = [2, 4, 6, 8]
# Output: [2,4,6]
print(find_common_list(arr1, arr2))

##############################################################################################
# find the first missing element in the array:


def first_missing_element(arr):
    for i in arr:
        curr = arr[i]
        next = arr[i + 1]
        if curr + 1 != next:
            return curr + 1


arr = [1, 2, 3, 4, 6, 7, 8]
# Output: 5
print(first_missing_element(arr))

##############################################################################################
# Find the first element of an array that is not consecutive (Not the missing element).


def first_non_consecutive(arr):
    for i in range(len(arr) - 1):
        curr = arr[i]
        next = arr[i + 1]
        if curr + 1 != next:
            return next
    return None


arr = [1, 2, 3, 4, 6, 7, 8]
# Output: 6
print(first_non_consecutive(arr))

#############################################################################################
# ways to convert list of ASCII value to string:


def covertListToString(nums):
    res = ''
    for char in nums:
        res += chr(char)
    return str(res)
###############################################
# Using map()


def covertListToString2(nums):
    res = ''.join(map(chr, myList))
    return str(res)

###############################################
# Using join and list comprehension


def covertListToString3(nums):
    res = ''.join(chr(char) for char in myList)
    return str(res)


# myList = [71, 101, 101, 107, 115, 102, 111, 114, 71, 101, 101, 107, 115]
myList = [65, 98, 100, 105, 102, 97, 116,
          97, 104, 77, 111, 104, 97, 109, 101, 100]
print(covertListToString(myList))

##########################################################################################################################################
# Two ways to map dictionary elements/characters in its index


def firstUniqChar(s: str) -> int:
    unique = {}
    for char in range(len(s)):
        unique[s[char]] = char

    # Another way using enumerate function:
    # for i, el in enumerate(s):
    #     unique[el] = i

    return unique


s = "leetcode"
print(firstUniqChar(s))

#########################################################################################################################################
# Find the first repeating character in the input string and return its index using dictionary HashMap:
# s = "leetcode" Output: 2 --> which e at index 2


def firstUniqChar(s: str) -> int:
    unique = {}
    for char in range(len(s)):
        if s[char] in unique:
            if unique[s[char]] == 1:
                return char
        else:
            unique[s[char]] = 1

s = "leetcode"
print(firstUniqChar(s))

#####################################################################################################################

