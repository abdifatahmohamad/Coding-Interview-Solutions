# Test Case 1:
# Input: likes = []
# Output: 'no one likes this'

# Test Case 2:
# Input: likes = ['Peter']
# Output: 'Peter likes this'

# Test Case 3:
# Input: likes = ['Jacob', 'Alex']
# Output: 'Jacob and Alex like this'

# Test Case 4:
# Input: likes = ['Max', 'John', 'Mark']
# Output: 'Max, John and Mark like this'

# Test Case 5:
# Input: likes = ['Alex', 'Jacob', 'Mark', 'Max']
# Output: 'Alex, Jacob and 2 others like this'

class Solution:
    def likes(self, names: str) -> str:
        if not names:
            return 'no one likes this'
        elif len(names) == 1:
            return f'{names[0]} likes this'
        elif len(names) == 2:
            return f'{names[0]} and {names[1]} like this'
        elif len(names) == 3:
            return f'{names[0]}, {names[1]} and {names[2]} like this'
        else:
            # return f'{names[0]}, {names[1]} and {len(names[1:])} others like this' # Don't use slicing coz it costs time
            return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'


solution = Solution()
# names = []
# names = ['Pater']
# names = ['Jacob', 'Alex']
names = ['Alex', 'Jacob', 'Mark', 'Max', 'Aaron']
print(solution.likes(names))
