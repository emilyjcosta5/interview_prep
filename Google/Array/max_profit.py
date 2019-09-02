"""
Author: Emily Costa
Created on: 8/31/2019
Best time to buy and sell stock.
Example.
Input: [1,2,3,4,5]
Output: 4
Buy on day 1 for 1 and sell on day 5 for 5 (5-1=4).
"""

import numpy as np

def max_profit(prices):
    i = 0
    for j in range(1, len(prices)):
        if i < j:
            buy = prices[i]
            j++
        if i > j:
            sell = prices[i]


