def sum_of_digits(n):
    total = 0
    n = abs(n)
    while n:
        total += n % 10
        n //= 10
    return total

number = int(input("Enter an integer: "))
print("sum of digits =", sum_of_digits(number))