def romanToInt(s: str) -> int:
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    for i in range(len(s)):
        curr = s[i]
        # nxt = s[i + 1]
        # i + 1 < len(s) checks if there's a character that comes after it, if it's true we compare the values
        # i + 1 < len(s) checks if next value is in bounds (range)
        # If current character followed by a large character, then the current is going to be negative
        # if (i + 1 < len(s)) and roman[curr] < roman[nxt]:
        if i + 1 < len(s) and roman[curr] < roman[s[i + 1]]:
            # Subtract result from current
            result -= roman[curr]
        else:
            # Add result from current
            result += roman[curr]
    return result


print(romanToInt("LVIII"))
print(romanToInt("XXVII"))
print(romanToInt("CMXCVIII"))
print(romanToInt("MCMXCIV"))
