"""
Question : Given an array of integers and positive integer k determine the number of (i,j) pairs where i <j
and ar(i) and ar(j) is divisible by k
date: 04 june 2020
Author : Pratiksha Mali
"""

n = 6  # length of ar
ar = [1, 3, 2, 6, 1, 2]
k = 3

"""
psudo code to get solution
1. create for loop 
2. to check i , j pair
3. check wheather sum of i, j pair is equal tp k
4. count pairs
"""

for i in ar:
    if min(ar) + max(ar)