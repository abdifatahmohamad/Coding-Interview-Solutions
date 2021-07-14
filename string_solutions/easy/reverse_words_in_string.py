def reverseWordsInString(s):
    sp = s.split()
    start = 0
    end = len(sp) - 1
    while start < end:
        # Swap helper function
        swap(sp, start, end)
        start += 1
        end -= 1
    return " ".join(sp)


# Create swap helper function:
def swap(s, left, right):
    temp = s[left]
    s[left] = s[right]
    s[right] = temp

################################################################
# Solving without creating swap function


def reverseWordsInString(s):
    sp = s.split()
    start = 0
    end = len(sp) - 1
    while start < end:
        sp[start], sp[end] = sp[end], sp[start]
        start += 1
        end -= 1
    return " ".join(sp)


st = "The sky is blue!"
print(reverseWordsInString(st))
