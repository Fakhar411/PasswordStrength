import streamlit as st
import re
import random
import pyperclip

# Weak passwords list
COMMON_PASSWORDS = {"password", "123456", "qwerty", "abc123", "password123", "letmein", "welcome", "admin", "123456789"}

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    if password.lower() in COMMON_PASSWORDS:
        return "❌ Too common! Choose a secure password.", "Weak", 10, "red"

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Must be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include uppercase & lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include a special character (!@#$%^&*).")

    strength_levels = [(10, "Weak", "red"), (40, "Fair", "orange"), (70, "Moderate", "gold"), (100, "Strong", "green")]
    return "\n".join(feedback) if score < 4 else "✅ Secure Password!", strength_levels[score][1], strength_levels[score][0], strength_levels[score][2]

# Generate strong password
def generate_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(12))

# Copy password to clipboard
def copy_to_clipboard(password):
    pyperclip.copy(password)
    st.success("✅ Password copied to clipboard!")

# Streamlit UI
st.set_page_config(page_title="🔐 Password Strength Meter", page_icon="🔒")
st.markdown("<h1 style='text-align: center;'>🔐 Password Strength Meter</h1>", unsafe_allow_html=True)

password = st.text_input("Enter your password:", type="password")
show_password = st.checkbox("👁 Show Password")
if show_password:
    st.write(f"🔑 Your Password: `{password}`")

if password:
    feedback, strength, progress, color = check_password_strength(password)
    st.progress(progress / 100)
    st.markdown(f"<h3 style='color: {color}; text-align: center;'>Strength: {strength}</h3>", unsafe_allow_html=True)
    st.write(feedback)

if st.button("🛠 Generate Strong Password"):
    strong_password = generate_password()
    st.text(f"🔑 Suggested Password: {strong_password}")
    if st.button("📋 Copy to Clipboard"):
        copy_to_clipboard(strong_password)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #00FFD1;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
