"""
Problem Statement: Given an integer N. Print the Fibonacci series up to the Nth term.

Example 1:
Input: N = 5
Output: 0 1 1 2 3 5
Explanation: 0 1 1 2 3 5 is the fibonacci series up to 5th term.(0 based indexing)

Example 2:
Input: 6

Output: 0 1 1 2 3 5 8
Explanation: 0 1 1 2 3 5 8 is the fibonacci series upto 6th term.(o based indexing)

"""

def fibonacci(n):
    
    if n == 0:
        return [0]

    if n == 1:
        return [0, 1]
    
    list = [0, 1]
    for i in range(2, n):
        list.append(list[-1] + list[-2])

    return list

#Driver Code
if __name__ == "__main__":
    n = int(input("enter n: "))
    print(fibonacci(n))