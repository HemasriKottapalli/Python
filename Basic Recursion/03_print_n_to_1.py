"""

Problem: Print from N to 1 using Recursion

"""

def print_1_to_n(n):

    #base condition
    if(n==0):
        return

    #processing
    print(n)

    #recursion call
    print_1_to_n(n-1)

#driver code
n = int(input("enter n: "))
print_1_to_n(n)