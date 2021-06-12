"""
Problem Statment: Given an array of integers and a positive integer k determin the number of(i,j) pairs where i < j and ar[i]
                   ar[j] is divisible by k
Author   : Pratiksha Mali
Data   : 12 june 2021
"""

def divisibleSumPair(n,k,ar):
    count = 0
    for i in range(len(ar)):
        for j in range(i+1,len(ar)):
            if((ar[i]+ar[j])%k)==0 and ar[i] < ar[j]:
                count +=1
    return count
