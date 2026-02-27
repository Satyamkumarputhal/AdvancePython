def palindrome_Check(s):
    reversed_str = s[::-1]
    if reversed_str == s:
        return f"{s} is palindrome."
    else:
        return f"{s} is not palindrome."

if __name__ == "__main__":
    user_input = input("Enter a String : ")
    result = palindrome_Check(user_input)
    print(result)