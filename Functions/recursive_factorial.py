def factorial(n):
    if(n==0):
        return 1
    elif(n==1):
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input("Enter a number : "))
fact = factorial(n)
print(f"factorial of {n} is {fact}")