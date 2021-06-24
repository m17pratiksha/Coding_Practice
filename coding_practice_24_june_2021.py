"""
Problem Statment: Given an array of bird sightings where every element
represents a bird type id,determine the id of the most frequently sighted type of more than 1 type has been
spotted that maximum amount return the smallest of their ids.
Author: Pratiksha Mali
Date: 24 june 2021
"""



def migrationofbirds(arr):
    """
    i expect this function should be able to analyse given array in following manner
    1) compare numbers in given array
    2) find numbers are repeating or not
    2) if yes , check how many times number is getting repeated
    3) find out smallest number amon those repeating numbers
    """
    same_type_birds = []

    for i in range(len(arr)):
        for j in range((i+1),len(arr)):

            if arr[i] == arr[j]:
                same_type_birds.append(arr[i])

    small_num = min(same_type_birds)

    return small_num

arr =[1,4,4,4,6,7]
print(migrationofbirds(arr))
