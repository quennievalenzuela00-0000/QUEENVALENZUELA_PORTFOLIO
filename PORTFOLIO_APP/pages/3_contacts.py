import streamlit as st
import time

st.set_page_config(page_title="Contact", layout="wide")

# Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
.main { 
    background: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 50%, #fbc2eb 100%);
    min-height: 100vh;
    padding: 3rem 2rem;
}
.contact-title {
    font-size: 4.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-bottom: 3rem;
}
.social-card {
    background: rgba(255,255,255,0.95);
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 2.5rem;
    margin: 1.5rem 0;
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    border: 1px solid rgba(255,255,255,0.3);
    transition: all 0.3s ease;
}
.social-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 30px 60px rgba(0,0,0,0.15);
}
.social-icon {
    font-size: 3rem;
    display: block;
    margin-bottom: 1rem;
}
.social-info {
    font-size: 1.3rem;
    color: #2c3e50;
    font-weight: 500;
}
.form-card {
    background: rgba(255,255,255,0.95);
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 3rem;
    box-shadow: 0 25px 50px rgba(0,0,0,0.15);
}
.form-title {
    font-size: 2rem;
    color: #2c3e50;
    margin-bottom: 2rem;
    text-align: center;
}
.form-input {
    width: 100%;
    padding: 1rem;
    border: 2px solid #e1e8ed;
    border-radius: 12px;
    font-size: 1.1rem;
    margin-bottom: 1.5rem;
    transition: border-color 0.3s ease;
}
.form-input:focus {
    border-color: #3498db;
    outline: none;
}
.success-message {
    background: linear-gradient(135deg, #56ab2f 0%, #a8e6cf 100%);
    color: white;
    padding: 2rem;
    border-radius: 16px;
    text-align: center;
    font-size: 1.2rem;
    font-weight: 600;
}
.nav-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
    margin-top: 3rem;
    flex-wrap: wrap;
}
.nav-btn {
    background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
    color: white;
    border: none;
    border-radius: 16px;
    padding: 1rem 2rem;
    font-weight: 600;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
}
.nav-btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 30px rgba(52,152,219,0.4);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="contact-title">MY CONTACT INFORMATION</h1>', unsafe_allow_html=True)

# Social Media Cards
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="social-card">
        <span class="social-icon">📘</span>
        <div class="social-info"><strong>FACEBOOK</strong></div>
        <div class="social-info">QUEEN VALENZUELA<br>QUEEN VILLARUEL</div>
    </div>
    
    <div class="social-card">
        <span class="social-icon">📱</span>
        <div class="social-info"><strong>PHONE NUMBER</strong></div>
        <div class="social-info">0981-658-1652</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="social-card">
        <span class="social-icon">✉️</span>
        <div class="social-info"><strong>GMAIL</strong></div>
        <div class="social-info">QUEEN00@GMAIL.COM</div>
    </div>
    
    <div class="social-card">
        <span class="social-icon">📲</span>
        <div class="social-info"><strong>OTHER PLATFORMS</strong></div>
        <div class="social-info">
            TELEGRAM: @queen_valenzuela<br>
            TIKTOK: @queen_vv<br>
            INSTAGRAM: @queen_valenzuela
        </div>
    </div>
    """, unsafe_allow_html=True)

# Contact Form
st.markdown("""
<div class="form-card">
    <h2 class="form-title">📝 Send Me a Message</h2>
""", unsafe_allow_html=True)

with st.form("contact_form"):
    name = st.text_input("Your Name", placeholder="Enter your name...")
    email = st.text_input("Your Email", placeholder="your.email@example.com")
    message = st.text_area("Message", placeholder="Tell me about yourself...", height=150)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        submitted = st.form_submit_button("🚀 Send Message", use_container_width=True)
    
    if submitted:
        if name and email and message:
            st.markdown("""
            <div class="success-message">
                ✅ Thank you for your message! I'll get back to you soon! ✨
            </div>
            """, unsafe_allow_html=True)
            st.balloons()
            time.sleep(2)
            st.rerun()
        else:
            st.error("❌ Please fill in all fields!")

st.markdown("</div>", unsafe_allow_html=True)

# Navigation Buttons (VS Code compatible)
st.markdown("""
<div class="nav-buttons">
    <button class="nav-btn" onclick="window.location.href='Home.py'">🏠 HOME</button>
    <button class="nav-btn" onclick="window.location.href='pages/2_👤_About.py'">👤 ABOUT</button>
    <button class="nav-btn" onclick="window.location.href='pages/4_🛠️_Skills.py'">🛠️ SKILLS</button>
    <button class="nav-btn" onclick="window.location.href='pages/5_❓_FAQ.py'">❓ FAQ</button>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <div style="font-size: 3rem;">👑</div>
        <h3 style="color: #2c3e50;">QUENNIE V. VALENZUELA</h3>
    </div>
    """, unsafe_allow_html=True)