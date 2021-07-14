def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    seen = {}
    for char in s.lower():
        # if char not in seen:
        #     seen[char] = 1
        # else:
        #     seen[char] += 1

        # Same above code but shorter way
        seen[char] = seen.get(char, 0) + 1
    for letter in t.lower():
        if letter not in seen:
            return False
        # Check if letters in hashmap is not contain more than 1 character
        if seen[letter] < 1:
            return False
        else:
            seen[letter] -= 1
    return True


print(isAnagram('Anagram', 'nagaRam'))  # True
print(isAnagram('moM', 'dAd'))
print(isAnagram('levEl', 'leeVl'))
