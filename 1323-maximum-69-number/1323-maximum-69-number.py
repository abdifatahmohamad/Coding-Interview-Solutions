class Solution:
    def maximum69Number (self, num: int) -> int:
        res = [n for n in str(num)]
        max_val = float("-Inf")
        for i in range(len(res)):
            prev = ''
            if res[i] == '9':
                res[i] = '6'
                prev = '9'
            elif res[i] == '6':
                res[i] = '9'
                prev = '6'
            max_val = max(max_val, int("".join(res)))
            res[i] = prev
            max_val = max(max_val, int("".join(res)))
        return max_val

        