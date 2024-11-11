"""
Problem: Print from 1 to N using Recursion

"""
def print_1_to_n(n):

    #base condition
    if(n==0):
        return
    
    #recursion call
    print_1_to_n(n-1)

    #processing
    print(n)


#driver code
n = int(input("enter n: "))
print_1_to_n(n)