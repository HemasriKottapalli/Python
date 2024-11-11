"""
Problem Statement: Given an integer N, return the number of digits in N.

Example 1:
Input:N = 12345
Output:5
Explanation:  The number 12345 has 5 digits.

Example 2:
Input:N = 7789
Output: 4
Explanation: The number 7789 has 4 digits.

"""

def count_digits(n):
    count = 0
    while n>0:
        n = n//10
        count = count+1
    return count

# # driver code
n = int(input("enter a number: "))
ans = count_digits(n)
print(f"the number has {n} has {ans} digits.")