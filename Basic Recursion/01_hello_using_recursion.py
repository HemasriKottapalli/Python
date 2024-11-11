"""
print hello n times using recursion

"""

def print_hello(n):
    # base condition
    if(n == 0):
        return
    
    #processing
    print("hello")
    
    #recursion call
    print_hello(n-1)

#driver code
n = int(input("enter a number"))
print(f"printing hello {n} times: \n")
print_hello(n)