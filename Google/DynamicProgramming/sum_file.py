"""
Author: Emily Costa
Created on: 8/30/2019
Write a function that sums up integers form a text file, one int per line.
"""

def sum_file(text_file):
    # solution
    sum = 0
    return sum

if __name__=="__main__":
    with open('num_file.txt', 'w') as w:
        nums = str((i+' ') for i in range(200))
        w.write(nums)
    text_file = 'num_file.txt'
    print(sum_file(text_file))

