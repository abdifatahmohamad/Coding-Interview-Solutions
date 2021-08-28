# Write a function that return sum of list of numbers in the array
# ignoring sections of numbers starting with a 6 and extending to the next 9
# (every 6 will be followed by at least one 9). Return 0 for no numbers.

# Test Case:
# number_69([1, 3, 5]) --> 9
# number_69([4, 5, 6, 7, 8, 9]) --> 9
# number_69([2, 1, 6, 9, 11]) --> 14

def number_69(arr):
    sum = 0
    stop = False
    for num in arr:
        if num == 6:
            stop = True
        elif num == 9:
            stop = False
        elif stop is False:
            sum = sum + num
    return sum


# Another way
def summer_69(arr):
    toSum = True
    sum = 0
    for x in arr:
        if toSum:
            if(x == 6):
                toSum = False
            else:
                sum += x
        else:
            if(x == 9):
                toSum = True
    return sum


print(number_69([2, 1, 6, 9, 11]))
