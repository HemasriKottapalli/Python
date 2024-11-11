"""
Problem Statement: Given an integer N, return all divisors of N.

A divisor of an integer N is a positive integer that divides N without leaving a remainder. In other words, if N is divisible by another integer without any remainder, then that integer is considered a divisor of N.

Example 1:
Input:N = 36
Output:[1, 2, 3, 4, 6, 9, 12, 18, 36]
Explanation: The divisors of 36 are 1, 2, 3, 4, 6, 9, 12, 18, 36.

Example 2:
Input:N =12
Output: [1, 2, 3, 4, 6, 12]
Explanation: The divisors of 12 are 1, 2, 3, 4, 6, 12.

"""

def list_divisors(number):
    list = []
    for i in range (1, number+1):
        if(number % i == 0):
            list.append(i)
    return list

#driver code
number = int(input("enter a number: "))
ans = list_divisors(number)
print(f"divisors of {number} are {ans}")