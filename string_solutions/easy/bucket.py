# https://learncodingfast.com/2-ways-to-convert-a-string-to-lowercase-in-python/
# Write a simple program to convert uppercase letters to lowercase
msg1 = 'HeLLo'
msg2 = ''

for i in msg1:
    # For each letter, we check if its Unicode code point is between 65 and 90.
    # If it is, we know that this is a uppercase character.
    if ord(i) >= 65 and ord(i) <= 90:
        # We then add 32 to the code point (ord(i) + 32) to get the code point
        # for the equivalent lowercase character.
        # We pass this result to the chr() function (chr(ord(i)+32))
        # and assign the result back to i
        i = chr(ord(i) + 32)
    msg2 += i

print(msg1)
print(msg2)


###################################################
# Write a function called myLower()
# that accepts a string and converts all the uppercase
# vowels = ("A", "E", "I", "O", "U") to lowercase.

def myLower(s):
    res = ""
    for i in s:  # if i equals ‘A’, ord(i) gives us the number 65 => a
        # For example, if i equals ‘B’, ord(i) gives the number 66 which is not inside the tuple. The if block is thus not executed.
        if ord(i) in (65, 69, 73, 79, 85):
            # This block converts the uppercase "AEIOU" to lowercase and assigns the result back to i
            i = chr(ord(i) + 32)
            res += i
    return res


print(myLower('AEIOU'))


###################################################
# Ways to initialize list with alphabets
# Run a loop till 26 and incrementing it while appending the letters in the list.
def alph():
    lst = []
    alpha = "a"
    for i in range(0, 26):
        lst.append(alpha)
        # Increment while appending the letters in the list
        alpha = chr(ord(alpha) + i)
    return lst


# Another way :
def alph():
    lst = []
    for c in range(ord('a'), ord('z') + 1):
        lst.append(chr(c))

    # using list comprehension for filling alphabets
    # lst = [chr(c) for c in range(ord('a'), ord('z') + 1)]
    return lst


print(alph())
