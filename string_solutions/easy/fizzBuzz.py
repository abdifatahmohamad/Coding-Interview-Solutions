from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for word in range(1, n+1):
            if word % 3 == 0 and word % 5 == 0:
                result.append('FizzBuzz')
            elif word % 3 == 0:
                result.append('Fizz')
            elif word % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(word))
        return result


solution = Solution()
print(solution.fizzBuzz(15))
