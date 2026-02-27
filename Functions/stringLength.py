def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

user = input("Enter a string: ")
print("length =", string_length(user))