import random

'''
given a sorted array of integers and a target integer, return the index of the integer 
or -1 if target does not exist in the array. 
'''

def r_binary_search(arr, num):
    def __k(arr,l,r):
        m = int((r-l)/2)+l
        if arr[m] == num:
            return m
        elif l >= r:
            return -1
        elif arr[m] < num:
            l = m+1
        elif arr[m] > num:
            r = m-1
        else:
            return -1
        return __k(arr, l, r)
    l,r = 0,len(arr)-1
    return __k(arr, l, r)

def binary_search(arr, num):
    l, r = 0, len(arr)-1
    
    while l <= r:
        m = int((r-l)/2)+l
        if arr[m] == num: 
             return m
        elif arr[m] < num: 
            l=m+1
        elif arr[m] > num:
            r=m-1 
        
    return -1
