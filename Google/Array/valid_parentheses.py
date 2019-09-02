"""
Author: Emily Costa
Created on: 9/2/2019
Given a string containing just the characters '('.')',...,']', determine if the input string is valid.
1. open brackets closed by same type of brackets
2. open brackets closed in correct order
"""

from collections import deque

def validate_string(string):
    if len(string) == 0:
        return True
    open_list = ['(','{','[']
    par_stack = deque()
    for par in string:
        print(par)
        if par in open_list:
            par_stack.append(par)
        elif par == ')':
            if par_stack.pop() != '(':
                return False
        elif par == '}':
            if par_stack.pop() != '{':
                return False
        elif par == ']':
            if par_stack.pop() != '[':
                return False
        else:
            print('something went wrong')
        print(par_stack)
    return True

if __name__=="__main__":
    str0 = '(())'
    str1 = '([})'
    print(validate_string(str0))
    print(validate_string(str1))

"""
Time complexity: O(n), iterates through array once.
Memory: O(1) to O(n), added memory created by stack
"""
