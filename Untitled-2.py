class Solution():
    """

    """
    def completed_bracket(self, order: str) -> bool:
        """
        returns True if the given string has complete brackets
        and False otherwise
        """
        stack = []
        first = set('([{')
        last = set('}])')

        pairs ={
        '(': ')',
        '[': ']',
        '{': '}',
        }
        for i in order:
            if i in first:
                stack.append(i)
            elif i in last:
                if not stack:
                    return False
                elif stack.pop() != pairs[i]:
                    return False
                else:
                    continue

        if not stack:
            return True
        else:
            return False            

if __name__ == '__main__':
    order = input("Enter a sequence of barackets and parentheses: ")
    print(f"Is {order} correct? : {Solution().completed_bracket(order)}")            