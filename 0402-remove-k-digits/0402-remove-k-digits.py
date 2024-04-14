class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []  # Initialize an empty stack to store digits
        
        # Iterate through each digit in the number
        for digit in num:
            # While there are still digits to remove (k > 0) and the stack is not empty
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()  # Remove digits from the stack until the top is smaller than the current digit
                k -= 1  # Decrement k since we removed a digit
            
            stack.append(digit)  # Add the current digit to the stack
        
        # If there are still digits to remove, remove them from the end of the stack
        while k > 0:
            stack.pop()
            k -= 1
        
        # Construct the result string from the stack, removing leading zeros
        result = ''.join(stack).lstrip('0')
        
        # If the result is empty, return '0'
        if not result:
            return '0'
        
        return result
        