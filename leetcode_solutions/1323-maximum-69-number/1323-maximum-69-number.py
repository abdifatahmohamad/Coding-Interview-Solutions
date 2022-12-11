class Solution:
    def maximum69Number (self, num: int) -> int:
        res = [n for n in str(num)]
        for i, c in enumerate(res):
            if c == '6':
                res[i] = '9'
                break
        return int("".join(res))

        