"""
Problem Statement: "Given a string, check if the string is palindrome or not."  A string is said to be palindrome if the reverse of the string is the same as the string.

Example 1:
Input: Str =  “ABCDCBA”
Output: Palindrome
Explanation: String when reversed is the same as string.

Example 2:
Input: Str = “TAKE U FORWARD”
Output: Not Palindrome
Explanation: String when reversed is not the same as string.

"""

def is_palindrome(string):
    original_string = string.lower()
    reversed_string = original_string[::-1]
    if(original_string == reversed_string):
        return True
    else:
        return False

#Driver Code
if __name__ == "__main__":
    string = "Heleh"
    ans = is_palindrome(string)
    print(f"is {string} a palindrome? {ans}")