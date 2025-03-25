
def is_palindrome(input_string):
   
    str = ''.join(input_string.split()).lower()
   
    return str == str[::-1]

input_string = input("Enter a string to check palindrome: ")

if is_palindrome(input_string):
    print(f"The string '{input_string}' is a palindrome.")
else:
    print(f"The string {input_string} is not a palindrome.")
