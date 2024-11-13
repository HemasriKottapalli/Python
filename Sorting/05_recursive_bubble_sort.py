"""
Problem Statement: Given an array of N integers, write a program to implement the Recursive Bubble Sort algorithm.

Example 1:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting we get 9,13,20,24,46,52

Example 2:
Input: N = 5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting we get 1,2,3,4,5
"""
def recursive_bubble_sort(arr, n):
    # Base case: If there is only one element, the array is already sorted
    if n == 1:
        return

    # One pass of bubble sort; the largest element moves to the end
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # Recursive call to sort the rest of the array
    recursive_bubble_sort(arr, n - 1)

# Example usage
arr1 = [13, 46, 24, 52, 20, 9]
arr2 = [5, 4, 3, 2, 1]

# Sort the arrays
recursive_bubble_sort(arr1, len(arr1))
recursive_bubble_sort(arr2, len(arr2))

# Print sorted arrays
print("Sorted array 1:", arr1)
print("Sorted array 2:", arr2)
