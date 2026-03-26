top_level_domains = [
    ".org",
    ".net",
    ".edu",
    ".ac",
    ".gov",
    ".com",
    ".io"
]


def validate_name(name):
    if type(name) == str and len(name) > 2:
        return True
    else:
        return False


def validate_email(email):
    if '@' not in email:
        return False
    for domain in top_level_domains:
        if domain in email:
            return True

    return False

user_name = input("Enter your name: ")
user_email = input("Enter your email: ")

if validate_name(user_name):
    print("Valid name.")
else:
    print("Invalid name. Name must be a string with more than 2 characters.")

if validate_email(user_email):
    print("Valid email.")
else:
    print("Invalid email. Email must contain '@' and end with a valid domain.")