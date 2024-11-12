"""
Problem Statement: Given an array of N integers, write a program to implement the Insertion sorting algorithm.

Example 1:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: 
After sorting the array is: 9,13,20,24,46,52

Example 2:
Input: N=5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting the array is: 1,2,3,4,5

"""
def insertion_sort(arr, n):
    # Traverse from the second element to the end of the array
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place key in its correct position
        arr[j + 1] = key

# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 5, 1, 9]
    n = len(arr)
    print(arr)
    insertion_sort(arr, n)
    print(arr)
