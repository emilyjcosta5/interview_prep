"""
Author: Emily Costa
Created on: 9/2/2019
Write a function that takes a string as input and reverse only the vowels of a string.
"""

from collections import deque

def reverse_vowels(word):
    vowel_stack = deque()
    vowels = ['a','e','o','u','i']
    for letter in word:
        if letter in vowels:
            vowel_stack.append(letter)
            print(letter)
    new_word = ''
    for letter in word:
        if letter in vowels:
            letter = vowel_stack.pop()
        new_word += letter
    return new_word

if __name__=="__main__":
    str0 = 'hello'
    str1 = 'hireme'
    print(reverse_vowels(str0))
    print(reverse_vowels(str1))

"""
Time complexity: O(2n), iterates through string twice
Memory: O(2n), saves two new arrays potentially size n
"""
