import streamlit as st
import re
import random

# Common weak passwords list
COMMON_PASSWORDS = {"password", "123456", "qwerty", "abc123", "password123", "letmein", "welcome", "admin", "123456789"}

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in COMMON_PASSWORDS:
        return "❌ Too common! Choose a secure password.", "Weak 😞", 0, "red"

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password must be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase & lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include one special character (!@#$%^&*).")

    # Strength Rating with Emoji & Progress Color
    if score == 5:
        return "✅ Strong Password! 😎", "Strong", 100, "#28a745"
    elif score >= 3:
        return "⚠️ Moderate Password 😐 - Improve security.", "Moderate", 60, "#ffc107"
    else:
        return "\n".join(feedback), "Weak 😞", 30, "#dc3545"

# Strong Password Generator
def generate_strong_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

# Streamlit UI
st.set_page_config(page_title="🔐 Password Strength Checker", page_icon="🔒", layout="centered")

st.markdown("<h1 style='text-align: center;'>🔐 Password Strength Meter</h1>", unsafe_allow_html=True)

# Show/Hide Password Feature
show_password = st.checkbox("👁 Show Password", value=False)
password = st.text_input("Enter your password:", type="text" if show_password else "password")

# Live Strength Indicator with Colored Progress Bar & Emoji
if password:
    feedback, strength, progress, color = check_password_strength(password)
    st.progress(progress / 100)  # Convert 0-100 to 0-1 for progress bar
    st.markdown(f"<h3 style='color: {color}; text-align: center;'>Strength: {strength}</h3>", unsafe_allow_html=True)
    st.write(feedback)

# Strong Password Generator Button
if st.button("🛠 Generate Strong Password"):
    strong_password = generate_strong_password()
    st.text("🔑 Suggested Strong Password: " + strong_password)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #00FFD1;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
