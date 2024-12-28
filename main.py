# Fibonacci function for nth number
def Fibonacci(n):
    if n<=0:
        print("Enter a positive number")
        # First fibonacci number is 0
    elif n ==1:
        return 0
        # Second fibonacci number is 1
    elif n ==2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
    
# Ask user for input
n = int(input("Enter a position in the Fibonacci sequence: "))

# Test the function    
print(Fibonacci(n))



