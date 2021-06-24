def valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    seen = {}
    for char in s:
        seen[char] = seen.get(char, 0) + 1

    for letter in t:
        if letter in seen:
            return True

        if seen[letter] < 1:
            return False
        else:
            seen[letter] -= 1

    return True


print(valid_anagram('Anagram', 'nagaram'))  # True
