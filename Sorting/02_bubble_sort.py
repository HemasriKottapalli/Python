"""
Problem Statement: Given an array of N integers, write a program to implement the Bubble Sorting algorithm.


Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting we get 9,13,20,24,46,52


Input: N = 5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting we get 1,2,3,4,5

"""
def bubble_sort(arr, n):
    for i in range(n):
        # Flag to detect any swap in this pass
        swapped = False
        for j in range(n-i):
            if( j+1 < n and arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no two elements were swapped, the array is already sorted       
        if swapped == False:
            break
            

# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 5, 1, 9]
    n = len(arr)
    print(arr)
    bubble_sort(arr, n)
    print(arr)