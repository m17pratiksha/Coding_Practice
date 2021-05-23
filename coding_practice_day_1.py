"""
Author: Pratiksha Mali
Date :  23 May 2021
Problem Statement : Divisible sum pairs
"""
'''

month = int(input("enter number"))

list1 = [1,2,3,4,5,6]

x = sum(list1[0:month])
print(x)

'''
#Solution for HackerRank subarray division problen
def subarraydiv(d,m,n:list):
    """
    d = day
    m = month
    n = number of squares
    """
    count = 0
    for i in range(len(n)):
        res = sum(n[i:i+m])
        #print(res)
        if res == d:
            count +=1
    return count

x = subarraydiv(3,2,[1,2,1,3,2])
print(x)
