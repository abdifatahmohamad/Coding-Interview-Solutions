def is_valid(parenthesis):
    stack = []
    mapping = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for p in parenthesis:
        if p in mapping:
            # If character at the top of the stack is matching the opening parenthesis in the hash map
            if stack and stack[-1] == mapping[p]:
                stack.pop()
            else:
                # Else if stack is empty or hash map doesn't have matching parenthesis
                return False
        else:
            stack.append(p)

    # At the end, after we gone through all characters, we can only return True if our stack
    # is empty, otherwise return False
    return not stack
    # return True if not stack else False


print(is_valid("()"))
# print(is_valid("()[]{}"))
# print(is_valid("(]"))
