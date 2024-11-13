"""
Problem Statement: Given an array of N integers, write a program to implement the Recursive Insertion Sort algorithm.

Example 1:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting we get 9,13,20,24,46,52

Example 2:
Input: N = 5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting we get 1,2,3,4,5

"""

def recursive_insertion_sort(arr, n):
    # Base case: If the array has one element or is empty, it is already sorted
    if n <= 1:
        return

    # Sort the first n-1 elements
    recursive_insertion_sort(arr, n - 1)

    # Insert the nth element into its correct position in the sorted part of the array
    last = arr[n - 1]
    j = n - 2

    # Move elements of arr[0..n-2], that are greater than last, to one position ahead
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = last

# Example usage
arr1 = [13, 46, 24, 52, 20, 9]
arr2 = [5, 4, 3, 2, 1]

# Sort the arrays
recursive_insertion_sort(arr1, len(arr1))
recursive_insertion_sort(arr2, len(arr2))

# Print sorted arrays
print("Sorted array 1:", arr1)
print("Sorted array 2:", arr2)
