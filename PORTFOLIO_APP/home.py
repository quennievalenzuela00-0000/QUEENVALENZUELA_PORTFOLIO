import streamlit as st
import time

# Page config
st.set_page_config(
    page_title="Queen's Portfolio",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS - PERFECT RESPONSIVE & NO LOADING TEXT
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');
    
* { 
    font-family: 'Poppins', sans-serif; 
    box-sizing: border-box;
}

.main { 
    background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 30%, #fecfef 70%, #a8edea 100%);
    min-height: 100vh;
    padding: 2rem 1rem;
    position: relative;
    overflow: hidden;
}

.main::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: 
        radial-gradient(circle at 20% 80%, rgba(120,119,198,0.25) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(255,119,198,0.25) 0%, transparent 50%),
        radial-gradient(circle at 40% 40%, rgba(120,219,255,0.25) 0%, transparent 50%);
    pointer-events: none;
    z-index: 0;
}

.content-wrapper {
    position: relative;
    z-index: 1;
    max-width: 1400px;
    margin: 0 auto;
}

/* RESPONSIVE HERO TITLE */
.hero-title {
    font-size: clamp(3rem, 8vw, 5.5rem);
    font-weight: 800;
    background: linear-gradient(135deg, #ff6b6b, #4ecdc4, #45b7d1, #f9ca24, #f0932b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    background-size: 300% 300%;
    animation: gradientShift 4s ease infinite;
    text-align: center;
    margin: 0 0 1.5rem 0;
    line-height: 1.1;
    text-shadow: 0 0 40px rgba(255,255,255,0.6);
    padding: 0 1rem;
}

@keyframes gradientShift {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

.subtitle {
    font-size: clamp(1.2rem, 4vw, 1.8rem);
    font-weight: 500;
    background: linear-gradient(135deg, #ffecd2, #fcb69f);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin: 1.5rem auto 3rem auto;
    line-height: 1.6;
    max-width: 800px;
    padding: 0 1rem;
}

.intro-card {
    background: rgba(255,255,255,0.18);
    backdrop-filter: blur(25px);
    border: 1px solid rgba(255,255,255,0.35);
    border-radius: 32px;
    padding: clamp(2rem, 5vw, 3.5rem);
    text-align: center;
    margin: 3rem auto;
    max-width: 700px;
    box-shadow: 0 25px 60px rgba(0,0,0,0.25);
    position: relative;
    overflow: hidden;
    transition: all 0.4s ease;
}

.intro-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 35px 80px rgba(0,0,0,0.35);
    border-color: rgba(255,255,255,0.5);
}

.intro-text {
    font-size: clamp(1.2rem, 3.5vw, 1.5rem);
    font-weight: 700;
    background: linear-gradient(135deg, #ffffff, #f0f8ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
    line-height: 1.6;
    text-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.arrow-animation {
    font-size: clamp(2rem, 6vw, 3.5rem);
    animation: bounceLeft 2s infinite;
    display: inline-block;
    background: linear-gradient(135deg, #ff6b6b, #4ecdc4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-shadow: 0 0 20px rgba(255,255,255,0.8);
}

@keyframes bounceLeft {
    0%, 20%, 50%, 80%, 100% { transform: translateX(0); }
    40% { transform: translateX(20px); }
    60% { transform: translateX(10px); }
}

.cta-section {
    text-align: center;
    margin: 5rem auto;
    padding: clamp(2rem, 6vw, 4rem) clamp(1rem, 4vw, 2rem);
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(20px);
    border-radius: 32px;
    border: 1px solid rgba(255,255,255,0.3);
    max-width: 800px;
}

.cta-title {
    font-size: clamp(1.8rem, 5vw, 2.5rem);
    background: linear-gradient(135deg, #ff6b6b, #feca57);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1rem;
    font-weight: 700;
}

.cta-subtitle {
    font-size: clamp(1.3rem, 4vw, 1.8rem);
    color: rgba(255,255,255,0.98);
    margin-bottom: 2rem;
    font-weight: 600;
}

/* SIDEBAR RESPONSIVE */
.sidebar .main .block-container {
    padding-top: 1rem;
}

.sidebar-header {
    background: linear-gradient(135deg, rgba(255,107,107,0.35), rgba(78,205,196,0.35));
    backdrop-filter: blur(25px);
    border-radius: 24px;
    padding: clamp(1.5rem, 4vw, 2.5rem) 1.5rem;
    margin-bottom: 2rem;
    border: 1px solid rgba(255,255,255,0.4);
    text-align: center;
    box-shadow: 0 20px 50px rgba(0,0,0,0.25);
}

.sidebar-header h2 {
    color: white !important;
    font-weight: 800 !important;
    margin: 0.5rem 0 0.3rem 0 !important;
    font-size: clamp(1.2rem, 3vw, 1.6rem) !important;
    text-shadow: 0 2px 10px rgba(0,0,0,0.3);
}

.sidebar-header p {
    color: rgba(255,255,255,0.95) !important;
    font-size: clamp(0.8rem, 2vw, 1rem) !important;
    font-weight: 500 !important;
    margin: 0 !important;
}

.sidebar-nav-btn {
    background: linear-gradient(135deg, rgba(255,255,255,0.2), rgba(255,255,255,0.1)) !important;
    backdrop-filter: blur(20px) !important;
    border: 1px solid rgba(255,255,255,0.3) !important;
    border-radius: 20px !important;
    padding: 1.2rem 1rem !important;
    margin: 0.8rem 0 !important;
    color: white !important;
    font-weight: 700 !important;
    font-size: clamp(1rem, 2.5vw, 1.2rem) !important;
    transition: all 0.3s ease !important;
    text-align: left !important;
    position: relative;
    overflow: hidden;
}

.sidebar-nav-btn:hover {
    background: linear-gradient(135deg, rgba(255,255,255,0.35), rgba(255,255,255,0.2)) !important;
    transform: translateX(8px) !important;
    box-shadow: 0 12px 30px rgba(0,0,0,0.3) !important;
    border-color: rgba(255,255,255,0.5) !important;
}

.sidebar-nav-btn:active {
    transform: translateX(4px) !important;
}
</style>
""", unsafe_allow_html=True)

# Main content wrapper
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# Hero Section - PERFECTLY RESPONSIVE
st.markdown('<h1 class="hero-title">WELCOME TO QUEEN&apos;S PORTFOLIO</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">A showcase of creativity, skills, and passion ✨</p>', unsafe_allow_html=True)

# Intro Card - FULLY RESPONSIVE
st.markdown("""
<div class="intro-card">
    <div class="intro-text">
        👑 <strong>I AM QUENNIE V. VALENZUELA</strong><br><br>
        📚 <strong>CURRENTLY TAKING BACHELOR OF SCIENCE IN COMPUTER SCIENCE</strong>
    </div>
</div>
""", unsafe_allow_html=True)

# CTA Section - RESPONSIVE
st.markdown("""
<div class="cta-section">
    <h2 class="cta-title">IF YOU WANT TO KNOW MORE ABOUT ME</h2>
    <p class="cta-subtitle">
        JUST CLICK THE BUTTONS IN THE SIDE 
        <span class="arrow-animation">👈</span>
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# PERFECT RESPONSIVE SIDEBAR
with st.sidebar:
    # Header
    st.markdown("""
    <div class="sidebar-header">
        <div style="font-size: clamp(3rem, 8vw, 4.5rem); margin-bottom: 0.8rem;">👑</div>
        <h2>QUENNIE&apos;S<br>PORTFOLIO</h2>
        <p>Explore my world ✨</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation Buttons - RESPONSIVE & STYLED
    if st.button("👤 ABOUT ME", key="about_btn", help="Personal information & journey"):
        st.session_state.page = "about"
        st.rerun()
    
    if st.button("🎯 CONTACT", key="contact_btn", help="Get in touch with me"):
        st.session_state.page = "contact"
        st.rerun()
    
    if st.button("🛠️ SKILLS", key="skills_btn", help="My talents and hobbies"):
        st.session_state.page = "skills"
        st.rerun()
    
    if st.button("❓ FAQ", key="faq_btn", help="Frequently asked questions"):
        st.session_state.page = "faq"
        st.rerun()