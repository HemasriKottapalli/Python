"""

Problem Statement: Given an integer N, return true if it is a palindrome else return false.

A palindrome is a number that reads the same backward as forward. For example, 121, 1331, and 4554 are palindromes because they remain the same when their digits are reversed.

Example 1:
Input:N = 4554
Output:Palindrome Number
Explanation: The reverse of 4554 is 4554 and therefore it is palindrome number

Example 2:
Input:N = 7789
Output: Not Palindrome
Explanation: The reverse of number 7789 is 9877 and therefore it is not palindrome

"""

def is_palindrome(number):
    original_number = number
    reversed_number = 0 

    while (number > 0):
        digit = number % 10
        reversed_number = reversed_number*10 + digit
        number = number // 10
    
    # return True if original_number == reversed_number else False
    # return original_numberr == reversed_number
    if(original_number == reversed_number):
        return True
    else:
        return False

#driver code
number = int(input("enter a number: "))
ans = is_palindrome(number)
print(f"Is {number} a palindrome? {ans}")