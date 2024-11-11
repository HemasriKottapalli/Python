"""

Problem statement: Given a number ‘N’, find out the sum of the first N natural numbers.

Example 1:
Input: N=5
Output: 15
Explanation: 1+2+3+4+5=15

Example 2:
Input: N=6
Output: 21
Explanation: 1+2+3+4+5+6=15

"""

def sum_of_n_nums(n):
    if n == 0 :
        return 0
    return n + sum_of_n_nums(n-1)

#driver code
n = int(input("enter n: "))
ans = sum_of_n_nums(n)
print(f"sum of first n numbers upto n is {ans}")