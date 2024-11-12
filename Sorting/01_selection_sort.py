"""
Problem Statement: Given an array of N integers, write a program to implement the Selection sorting algorithm.

Example 1:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting the array is: 9, 13, 20, 24, 46, 52

Example 2:
Input: N=5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting the array is: 1, 2, 3, 4, 5
"""
def selection_sort(arr, n):
    for i in range(n):
        # Assume the minimum element is at the current position i
        min_index = i
        # Find the minimum element in the unsorted part of the array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the element at position i
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
#Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 5, 1, 9]
    n = len(arr)
    print(arr)
    selection_sort(arr, n)
    print(arr)