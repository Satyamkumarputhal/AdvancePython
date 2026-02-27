def vowelCount(str):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    count = 0

    for i in str:
        if(i in vowels):
            count+=1
    return count

str = input("Enter a string : ")
vowel_check = vowelCount(str)
if(vowel_check>1):
    print(f"No. of vowels in {str} is {vowel_check}")
else:
    print(f"There are 0 vowels in {str}")