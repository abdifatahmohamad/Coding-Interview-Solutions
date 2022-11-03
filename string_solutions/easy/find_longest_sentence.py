def longestSentence(sentences):
    longest = float("-Inf")
    for sentence in sentences:
        length = get_word_length(sentence)
        longest = max(longest, length)
    return longest


def get_word_length(sentence):
    count = 0
    for ch in sentence:
        if ch != " ":
            count += 1
    return count


# Solution counting spaces:
def longestSentence(sentences):
    longest = float("-Inf")
    for sentence in sentences:
        length = get_word_length(sentence)
        longest = max(longest, length)
    return longest


def get_word_length(sentence):
    count = 0
    for ch in sentence:
        if ch == " ":
            count += 1
    return count + 1


print(get_word_length(["hi", "hello world", "lets do leetcode"]))

print(longestSentence([" lets do leetcode",
                       "am going to play soccer", "am on vacation"]))
print(longestSentence(["hi", "hello world", "lets do leetcode"]))
