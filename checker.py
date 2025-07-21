import re

def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        'Length': length_error,
        'Uppercase': uppercase_error,
        'Lowercase': lowercase_error,
        'Digit': digit_error,
        'Special Character': special_char_error
    }

    if not any(errors.values()):
        strength = "Strong"
    elif sum(errors.values()) == 1:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, errors

# Main program

user_password = input("Enter your password: ")
strength, issues = check_password_strength(user_password)

print(f"\nPassword Strength: {strength}")

if strength != "Strong":
    print("Suggestions:")
    for rule, failed in issues.items():
        if failed:
            print(f" - Add {rule}")
