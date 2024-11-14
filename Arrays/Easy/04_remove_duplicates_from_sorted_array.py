"""
Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.

If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.

Note: Return k after placing the final result in the first k slots of the array.

Example 1:
Input:
 arr[1,1,2,2,2,3,3]

Output:
 arr[1,2,3,_,_,_,_]

Explanation:
 Total number of unique elements are 3, i.e[1,2,3] and Therefore return 3 after assigning [1,2,3] in the beginning of the array.

Example 2:
Input:
 arr[1,1,1,2,2,3,3,3,3,4,4]

Output:
 arr[1,2,3,4,_,_,_,_,_,_,_]

Explanation:
 Total number of unique elements are 4, i.e[1,2,3,4] and Therefore return 4 after assigning [1,2,3,4] in the beginning of the array.
"""
#Brute Force
def remove_duplicates(arr):
    st = set()

    for i in range(len(arr)):
        st.add(arr[i])
    
    for i in range(len(st)):
        arr[i] = st[i]
        
    return len(st)

#Driver Code
arr = [1,2,3,4,5,1,3,4,5]
no_of_unique_elements = remove_duplicates(arr)
print(f'no of unique elements: {no_of_unique_elements}')