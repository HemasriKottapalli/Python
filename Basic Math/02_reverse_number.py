"""
Problem Statement: Given an integer N return the reverse of the given number.

Note: If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.

Example 1:
Input:N = 12345
Output:54321
Explanation: The reverse of 12345 is 54321.
Example 2:
Input:N = 7789
Output: 9877
Explanation: The reverse of number 7789 is 9877.

"""

def reverse_number(number):
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number*10 + digit
        number = number//10
    return reversed_number

#driver code
number = int(input("Enter a number: "))
ans = reverse_number(number)
print(f"reversed number is: {ans}")