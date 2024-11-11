"""
Problem Statement: Given an integer N, return true it is an Armstrong number otherwise return false.

An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

Example 1:
Input:N = 153
Output:True
Explanation: 13+53+33 = 1 + 125 + 27 = 153

Example 2:
Input:N = 371
Output: True
Explanation: 33+53+13 = 27 + 343 + 1 = 371

"""

# from _01_count_digits import count_digits

def count_digits(n):
    count = 0
    while n>0:
        n = n//10
        count = count+1
    return count

def is_armstrong_number(number):
    power = count_digits(number)
    sum = 0
    original_number = number

    while number>0 :
        digit = number % 10
        sum = sum + (digit ** power)
        number = number//10

    # if original_number == sum:
    #     return True
    # else :
    #     return False

    return True if(original_number == sum) else False

#driver code
number = int(input("Enter a number: "))
ans = is_armstrong_number(number)
print(f"is {number} an armstrong number? {ans}")