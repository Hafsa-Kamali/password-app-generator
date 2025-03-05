import streamlit as st
import re

def calculate_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Include uppercase letters")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Include lowercase letters")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add at least one number")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Include at least one special character")
    
    if score == 5:
        strength = "Strong"
        color = "#2ECC71"
    elif score >= 3:
        strength = "Medium"
        color = "#F39C12"
    else:
        strength = "Weak"
        color = "#E74C3C"
    
    return score, strength, color, feedback

def main():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background:
            url('https://t3.ftcdn.net/jpg/06/27/48/84/360_F_627488418_f0wbIZoJt2bsLBgDweP0w6ycmibqHGbZ.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        
        .title {{
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 20px;
            color: #D3D3D3;
        }}
        .stTextInput > div > div > input {{
            background-color: rgba(255,255,255,0.9);
            border: 2px solid #3498DB;
            color: black;
            border-radius: 10px;
        }}
        .stButton > button {{
            background-color: #3498DB;
            color: white;
            border-radius: 10px;
            transition: all 0.3s ease;
        }}
        .stButton > button:hover {{
            background-color: #2980B9;
            transform: scale(1.05);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="title">🔐 Password Strength Checker</div>', unsafe_allow_html=True)
    
    password = st.text_input("Enter your password", type="password")
    
    if st.button("Generate  Password"):
        if password:
            score, strength, color, feedback = calculate_password_strength(password)
            
            st.progress(score * 20)
            
            st.markdown(f'<h3 style="color:{color};">{strength} Password</h3>', unsafe_allow_html=True)
            
            if feedback:
                st.markdown("**Suggestions to Improve:**")
                for suggestion in feedback:
                    st.markdown(f"❌ {suggestion}")
            else:
                st.markdown("✅ Strong password! You're all set.")
        else:
            st.error("Please enter a password first.")

if __name__ == "__main__":
    main()
