"""
Problem Statement: Given an array of size N. Find the highest and lowest frequency element.

Example 1:
Input: array[] = {10,5,10,15,10,5};
Output: 10 15
Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.

Example 2:
Input: array[] = {2,2,3,4,4,2};
Output: 2 3
Explanation: The frequency of 2 is 3, i.e. the highest and the frequency of 3 is 1 i.e. the lowest.

"""
def get_min_max_freequencies(arr):
    map = {}
    for i in range(len(arr)):
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1
    
    # finding min and max repeated elements
    min_freequency = min(map.values())
    max_freequency = max(map.values())

    for key, value in map.items():
        if value == min_freequency:
            min_repeated_value = key
        if value == max_freequency:
            max_repeated_value = key

    return min_repeated_value, max_repeated_value

#driver code
if __name__=="__main__":
    arr = [10, 2, 2, 3, 4, 5, 3, 2, 4, 10, 20, 5, 20]
    min, max = get_min_max_freequencies(arr)
    print(min, max)