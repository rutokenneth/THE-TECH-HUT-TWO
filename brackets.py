import collections

class Solution():
    """
    A class to represent a solution to the problem of checking
    if a string has complete brackets.
    """

    def __init__(self):
        self.pairs = collections.defaultdict(lambda: None,{
            '(': ')',
            '[': ']',
            '{': '}',
        })

    def completed_bracket(self, brackets_list: str) -> bool:
        """
        Returns True if the given string has complete brackets and False otherwise.

        Args:
            order: A string representing a sequence of brackets and parentheses

        Returns:
            True or False
        """ 
        stack = []
        first = set('([{')
        last = set('}])')

        for i in brackets_list:
            if i in first:
                stack.append(i)
            elif i in last:
                if not stack or stack.pop() != self.pairs[i]:
                    return False
                else:
                    continue
                return not stack

if __name__ == '__main__':
    try:
        brackets_list = input("Enter a sequence of brackets and parentheses: ")
        print(Solution().completed_bracket(brackets_list))
    except Exception as e:
        print(e)               