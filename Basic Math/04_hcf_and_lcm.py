"""
Problem Statement: Given two integers N1 and N2, find their greatest common divisor.

The Greatest Common Divisor of any two integers is the largest number that divides both integers.

Example 1:
Input:N1 = 9, N2 = 12               
Output:3
Explanation:Factors of 9: 1, 3 and 9
Factors of 12: 1, 2, 3, 4, 6, 12
Common Factors: 1, 3 out of which 3 is the greatest hence it is the GCD.

Example 2:
Input:N1 = 20, N2 = 15                
Output: 5
Explanation:Factors of 20: 1, 2, 4, 5
Factors of 15: 1, 3, 5
Common Factors: 1, 5 out of which 5 is the greatest hence it is the GCD.

extra: calculate lcm too
"""

def get_hcf(number1, number2):
    for i in range(max(number1, number2), 0, -1):
        if(number1%i == 0 and number2%i == 0):
            return i
        
# LCM(a,b)= ∣a×b∣/GCD(a,b)
def get_lcm(number1, number2):
    return abs(number1*number2)/get_hcf(number1, number2)

#driver code
number1, number2 = map(int, input("Enter two numbers separated by a space: ").split())
hcf = get_hcf(number1, number2)
lcm = get_lcm(number1, number2)
print(f"HCF of {number1} and {number2} is {hcf} and LCM is {int(lcm)}")



