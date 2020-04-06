# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 11:24:16 2020

@author: Magzh
"""

# Merge Sort
def mergeSort(arr):
    size = len(arr)
    # creating an empty temporary array that will store new values after each mergeSort cycle
    temp = [0]*size
    sort(arr, temp, 0, size - 1)
    

def sort(arr, temp, LeftIndex, RightIndex):
    # Checking whether it reached array of size 1
    if LeftIndex != RightIndex:
        # Searching for the mid point of the array
        MiddleIndex = (LeftIndex + RightIndex) // 2
        # Sorting out Left side
        sort(arr, temp, LeftIndex, MiddleIndex)
        # Sorting out Right side
        sort(arr, temp, MiddleIndex + 1, RightIndex)
        # Merging sorted sides together
        merge(arr, temp, LeftIndex, MiddleIndex, RightIndex)

def merge(arr, temp, LeftIndex, MiddleIndex, RightIndex):
    currentLeft = LeftIndex # starting point of left side
    currentRight = MiddleIndex + 1 # starting point of right side
    currentMerge = LeftIndex # starting point of merged part
    # This while loop goes trhough already sorted sides one by one until one of the sides runs out of values to assign
    while currentLeft <= MiddleIndex and currentRight <= RightIndex:
        if arr[currentLeft] <= arr[currentRight]:
            temp[currentMerge] = arr[currentLeft]
            currentMerge += 1
            currentLeft += 1
        else:
            temp[currentMerge] = arr[currentRight]
            currentMerge += 1
            currentRight += 1
    # Next two while loops go through whichever indexes got left unassigned in the previous while loop
    while currentLeft <= MiddleIndex:
        temp[currentMerge] = arr[currentLeft]
        currentMerge += 1
        currentLeft += 1
    while currentRight <= RightIndex:
        temp[currentMerge] = arr[currentRight]
        currentMerge += 1
        currentRight += 1
    # Now iterating through every merged sorted index and reassigning them back to the original array
    for x in range(LeftIndex, RightIndex + 1):
        arr[x] = temp[x]
