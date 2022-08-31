class Solution:
    def compress(self, chars: List[str]) -> int:
        index, count = 0, 1
        for j in range(1, len(chars) + 1):
            if j < len(chars) and chars[j] == chars[j - 1]:
                count += 1
            else:
                chars[index] = chars[j - 1]
                index += 1
                if count > 1:
                    for k in str(count):
                        chars[index] = k
                        index += 1
                count = 1
        return index