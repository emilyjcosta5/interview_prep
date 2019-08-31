"""
Author: Emily Costa
Created on: 8/31/2019
Given a sorted array, remove duplicated in-place such that each element will only appear once and function returns length.
"""

import numpy as np

def remove_duplicates(array):
    # solution
    # np.delete(arr, obj)
    # first pointer
    i = 0
    # all the indexes of the values that should be removed
    ind = []
    for j in range(1, array.size):    
        if array[i] == array[j]:
            ind.append(j)
            j += 1
        else:
            i = j
            j += 1
    array = np.delete(array, ind)
    return array.size

if __name__=="__main__":
    # test implementation
    sorted_array = np.sort(np.random.randint(low=1,high=100,size=10000))
    print(remove_duplicates(sorted_array))
    # expected output: 99

"""
Time complexity: O(n)
Memory: O(1)
"""

