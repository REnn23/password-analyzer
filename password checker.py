import re

def password_validator(password):
    # Check if password has 8 characters
    if len(password)< 8:
        return "Password must be at least 8 characters long"
    if not re.search(r'[A-Z]', password):  # Check if password has at least one uppercase letter
        return "Password must contain at least one uppercase letter"
    if not re.search(r'[a-z]', password):  # Check if password has at least one lowercase letter
        return "Password must contain at least one lowercase letter"
    if not re.search(r'\d', password):  # Check if password has at least one digit
        return "Password must contain at least one digit"
    if not re.search(r'[!@#$%&]', password):  # Check if password has at least one special character
        return "Password must contain at least one special character"

    return "password meets requirements"

if __name__ == "__main__":
    password = input("Enter your password: ")
    is_valid = password_validator(password)
    print(is_valid)


        