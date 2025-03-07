import streamlit as st
import re

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")
    
    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")
    
    # Number check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number.")
    
    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&* etc.).")
    
    # Strength classification
    if score >= 5:
        strength = "Strong"
        color = "green"
    elif score >= 3:
        strength = "Medium"
        color = "blue"
    else:
        strength = "Weak"
        color = "red"
    
    return strength, color, feedback

st.title("Password Strength Meter 🔒")
password = st.text_input("Enter your password to see its strength:", type="password")

if password:
    strength, color, feedback = check_password_strength(password)
    st.markdown(f"**Strength:** <span style='color:{color}; font-weight:bold;'>{strength}</span>", unsafe_allow_html=True)
    
    if feedback:
        st.warning("\n".join(feedback))
st.write("------------------------")
st.write("Made with ❤️ by [Mudasir Sohail](https://www.linkedin.com/in/mudasir-sohail-98b399257/)")