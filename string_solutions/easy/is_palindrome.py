class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            # Both while loops will make sure both compared characters
            # is alpha numeric

            # left < right condition make sure that the left pointer
            # never goes out of pound (never passes the R pointer)
            while left < right and not self.alpha_numeric(s[left]):
                left += 1

            while right > left and not self.alpha_numeric(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True

    # Create our own alpha numerical function
    def alpha_numeric(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))
