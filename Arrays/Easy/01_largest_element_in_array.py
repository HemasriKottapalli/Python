"""
Problem Statement: Given an array, we have to find the largest element in the array

Example 1:
Input:
 arr[] = {2,5,1,3,0};
Output:
 5
Explanation:
 5 is the largest element in the array. 

Example2:
Input:
 arr[] = {8,10,5,7,9};
Output:
 10
Explanation:
 10 is the largest element in the array. 

"""

# def find_max(arr):
#     return max(arr)

def find_max(arr):
    n = len(arr)
    max = float('-inf') # Negative Infinity

    for i in range(n):
        if arr[i] > max:
            max = arr[i]
    return max

#Driver Code
arr = [1,2,4,6,4,9]
ans = find_max(arr)
print(f"max element in arr is : {ans}")