import re

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(email_regex, email):
        return True
    else:
        return False
    
email = input("Enter an email to validate: ")

if is_valid_email(email):
    print("Valid email address.")
else:
    print("Invalid email address.")
