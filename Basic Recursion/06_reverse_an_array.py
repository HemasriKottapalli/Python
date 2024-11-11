"""
Problem Statement: You are given an array. The task is to reverse the array and print it. 

Example 1:
Input: N = 5, arr[] = {5,4,3,2,1}
Output: {1,2,3,4,5}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

Example 2:
Input: N=6 arr[] = {10,20,30,40}
Output: {40,30,20,10}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

"""
def print_array(arr):
    for i in arr:
        print(i, end=" ")

def reverse_arr(arr, start, end):
    # Base case: if start is greater than or equal to end, the array is reversed
    if start >= end:
        return
    # Swap the elements at positions 'start' and 'end'
    arr[start], arr[end] = arr[end], arr[start]
    # Recursively reverse the subarray excluding the swapped elements
    reverse_arr(arr, start + 1, end - 1)
    
#Driver Code
if __name__ == "__main__":
    arr = [1,2,3,4,5]
    n = len(arr)
    print("Original Array: ")
    print_array(arr)
    reverse_arr(arr, 0, n-1)
    print("\nReversed Array: ")
    print_array(arr)