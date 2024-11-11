"""
Problem statement: Given an array, we have found the number of occurrences of each element in the array.

Example 1:
Input: arr[] = {10,5,10,15,10,5};
Output: 10  3
	    5  2
        15  1
Explanation: 10 occurs 3 times in the array
	         5 occurs 2 times in the array
            15 occurs 1 time in the array


Example2: 
Input: arr[] = {2,2,3,4,4,2};
Output: 2  3
	    3  1
        4  2
Explanation: 2 occurs 3 times in the array
	        3 occurs 1 time in the array
            4 occurs 2 time in the array
"""

# nested loop approach  T.C : n^2
def count_freequency_through_loop(arr):
    visited = [False]*len(arr)
    for i in range(0, len(arr)):
        if visited[i] == True:
            continue
        count = 1
        for j in range(i+1, len(arr)):
            if(arr[i] == arr[j]):
                visited[j] = True
                count += 1
        print(arr[i], count)
        
# hashmap(dictionary) approach T.C: n
def count_freequency_through_map(arr):
    map = {}
    n = len(arr)
    for i in range(n):
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1

    for i in map:
        print(i, map[i])

#Driver code
if __name__ == "__main__":
    arr = [10, 2, 3, 5, 10, 3, 4]
    # count_freequency_through_loop(arr)
    count_freequency_through_map(arr)
