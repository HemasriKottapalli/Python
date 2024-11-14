"""
Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.

Example 1:
Input:
 [1,2,4,7,7,5]
Output:
 Second Smallest : 2
	Second Largest : 5
Explanation:
 The elements are as follows 1,2,3,5,7,7 and hence second largest of these is 5 and second smallest is 2

Example 2:
Input:
 [1]
Output:
 Second Smallest : -1
	Second Largest : -1
Explanation:
 Since there is only one element in the array, it is the largest and smallest element present in the array. There is no second largest or second smallest element present.

"""

def solve(arr):
    n = len(arr)

    if n < 2:
        return -1,-1
    
    min_val = float('inf')
    second_min = float('inf')
    max_val = float('-inf')
    second_max = float('-inf')


    for i in range(n):
        if(arr[i] < min_val):
            second_min = min_val
            min_val = arr[i]
        elif (arr[i] < second_min):
            second_min = arr[i]
    
    for i in range(n):
        if(arr[i] > max_val):
            second_max = max_val
            max_val = arr[i]
        elif (arr[i] > second_max):
            second_max = arr[i]

    return second_min, second_max

#Driver Code
arr = [1, 2, 3, 6, 4, 8]
second_small, second_large = solve(arr)
print(f"Second small element in array is {second_small} and Second large element in array is {second_large}")