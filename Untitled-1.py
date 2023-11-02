class solution():
    def completed(self, order):
        '''
        funtion that checks if a string has complete brackets
        '''
        stack = []
        first = set('([{')
        last = set('}])')

        pairs = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        for i in order:
            if i in first:
                stack.append(i)
            if i in last:
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
    print(f"Is {order} correct? : {solution().completed(order)}")
    