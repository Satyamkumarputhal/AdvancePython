def fibonacci(n):
    if n <= 0:
        return []
    seq = [0]
    if n == 1:
        return seq
    seq.append(1)
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

count = int(input("Enter nth term : "))
print(fibonacci(count))