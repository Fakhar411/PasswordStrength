import streamlit as st
import re
import random

# Common weak passwords list
COMMON_PASSWORDS = ["password", "123456", "12345678", "qwerty", "abc123", "password123"]

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in COMMON_PASSWORDS:
        return "❌ This password is too common! Choose a more secure one.", "Weak"

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 5:
        return "✅ Strong Password!", "Strong"
    elif score >= 3:
        return "⚠️ Moderate Password - Consider adding more security features.", "Moderate"
    else:
        return "\n".join(feedback), "Weak"

# Function to generate a strong password
def generate_strong_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

# Streamlit UI
st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password:", type="password")

if st.button("Check Strength"):
    if password:
        feedback, strength = check_password_strength(password)
        st.subheader("Password Strength: " + strength)
        st.write(feedback)

# Strong Password Generator
if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.text("🔑 Suggested Strong Password: " + strong_password)
