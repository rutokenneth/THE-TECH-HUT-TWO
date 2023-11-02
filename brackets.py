def valid_parentheses(s):
    """
    Checks if user input forms a valid bracket pair

    Args:
        takes user-input bracket sequence
    returns:
        Boolean Values True or False    
    """
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

s = input("Enter a string of brackets: ")
print(valid_parentheses(s))