"""
Problem Statement: Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.

Note: Two consecutive equal values are considered to be sorted.

Example 1:
Input:
 N = 5, array[] = {1,2,3,4,5}
Output
: True.
Explanation:
 The given array is sorted i.e Every element in the array is smaller than or equals to its next values, So the answer is True.

"""

def is_ascending_order(arr, n):
    for i in range(n-1):
        if arr[i] <= arr[i+1]:
           continue
        else:
             return False
    return True


def is_descending_order(arr,n):
    for i in range(n-1):
        if arr[i] >= arr[i+1]:
            continue
        else:
             return False
    return True


#Driver Code
arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
is_sorted = is_ascending_order(arr, n) or is_descending_order(arr,n)
print(f'is array sorted? {"yes" if is_sorted else "no"}')