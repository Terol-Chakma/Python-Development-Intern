
#Task 1 : string reversal.
def reverse_string():
    str = input("Enter a string to reverse: ")
    if not str:
        return "Sorry!!! there is no input. please enter a string."
    return str[::-1]

print("The reversed string is: ", reverse_string())
