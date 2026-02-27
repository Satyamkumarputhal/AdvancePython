def largest(numbers):
    return max(numbers)

n = input("Enter numbers in the list (separated by spaces): ")
nums = [int(i) for i in n.split()]
print(f"The largest number in the list is {largest(nums)}")