"""
Problem Statement:  Given an array of n integers, sort the array using the Quicksort method.

Example 1:
Input:  N = 5  , Arr[] = {4,1,7,9,3}
Output: 1 3 4 7 9 
Explanation: After sorting the array becomes 1, 3, 4, 7, 9

Example 2:
Input: N = 8 , Arr[] = {4,6,2,5,7,9,1,3}
Output: 1 2 3 4 5 6 7 9
Explanation: After sorting the array becomes 1, 3, 4, 7, 9

"""
def partition(arr, low, high):
    pivot = arr[high]  # choose the rightmost element as pivot
    i = low - 1  # pointer for the smaller element

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap if element is smaller than pivot

    # place the pivot element at the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        # partition the array
        pi = partition(arr, low, high)

        # recursively sort elements before and after partition
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

# Example usage
arr1 = [4, 1, 7, 9, 3]
arr2 = [4, 6, 2, 5, 7, 9, 1, 3]

# Sort the arrays
quicksort(arr1, 0, len(arr1) - 1)
quicksort(arr2, 0, len(arr2) - 1)

# Print sorted arrays
print("Sorted array 1:", arr1)
print("Sorted array 2:", arr2)
