import re

def assess_password_strength(password):
    feedback = []
    score = 0

    # Criteria checks
    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Make it at least 12 characters long.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    if re.search(r'[^A-Za-z0-9]', password):
        score += 1
    else:
        feedback.append("Add at least one special character (e.g., !@#$%^&*).")

    # Strength evaluation
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Results
    print(f"Password Strength: {strength}")
    if feedback:
        print("Suggestions to improve your password:")
        for f in feedback:
            print(f"- {f}")

user_password = input("Enter a password to check: ")
assess_password_strength(user_password)

