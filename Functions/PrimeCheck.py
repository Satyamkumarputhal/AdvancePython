def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is prime")
else:
    print(num, "is not prime")