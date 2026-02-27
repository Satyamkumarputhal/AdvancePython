# 1. write a program to take a string input from the user and print it in reverse.
# 2. Write a program to count the numbers of uppercase and lowercase characters in a String.
# 3. Write a program to check whether a given string contains only digits.
# 4. Write a program to replace all spaces in a string with underscore.
# 5. write a program to count the frequency of each character in a String.
# 6. Write a program to find the first and last occurrence of a character in a string.
# 7. Write a program to remove all vowels from a given string.
# 8. Write a program to check whether two strings are anagrams of each other.
# 9. Write a program to capitalize the first letter of each word in a string.
# 10.Write a program to check whether a given string is a palindrome without using built-in reverse functions.

# 1. String reversal
# str = input ("Enter a string : ")
# rev = str[::-1]
# print (rev)

# #2. count uppercase & lowercase
# input_str = input ("Enter a string : ")
# uppercase = 0
# lowercase = 0

# for i in input_str:
#     if (ord(i) in range(65,91)):
#         uppercase += 1
#     elif (ord(i) in range (97,123)):
#         lowercase += 1

# print(f"count of uppercase characters : {uppercase}")
# print(f"count of lowercase characters : {lowercase}")


#3. String contains only digits
# input_str = input("Enter a string: ")

# if input_str.isdigit():
#     print("The string contains only digits")
# else:
#     print("The string does not contain only digits")

#4. replace spaces with underscore
# import re
# input_str = input("Enter a string : ")
# result = re.sub(r" ", "_", input_str)
# print(result)

#5. frequency of a character
# input_str = input("Enter a string: ")
# count = {}

# for i in input_str:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1
# print(count)
        



