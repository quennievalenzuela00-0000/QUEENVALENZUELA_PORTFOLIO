import streamlit as st
import time

st.set_page_config(page_title="About Me - Queen's Portfolio", layout="wide")

# Custom CSS - Professional UI/UX
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
* { font-family: 'Poppins', sans-serif; }
.main { 
    background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
    min-height: 100vh;
    padding: 3rem 2rem;
}

.about-title {
    font-size: 4.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-align: center;
    margin-bottom: 3rem;
    line-height: 1.1;
}

.info-card {
    background: rgba(255,255,255,0.95);
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 3rem;
    margin: 2rem 0;
    box-shadow: 0 25px 50px rgba(0,0,0,0.15);
    border: 1px solid rgba(255,255,255,0.3);
    transition: all 0.3s ease;
}

.info-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 35px 70px rgba(0,0,0,0.2);
}

.info-title {
    font-size: 1.8rem;
    font-weight: 700;
    color: #2c3e50;
    margin-bottom: 1.5rem;
    padding-bottom: 1rem;
    border-bottom: 3px solid #3498db;
    text-align: center;
}

.info-title.black-title {
    color: #000000 !important;
}

.info-detail {
    font-size: 1.3rem;
    color: #34495e;
    line-height: 1.8;
    margin: 1.2rem 0;
    padding: 0.5rem 1rem;
    background: rgba(255,255,255,0.7);
    border-radius: 12px;
}

.personal-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
}

.family-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
}

.family-card {
    background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
    border-radius: 20px;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 15px 35px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
}

.family-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 25px 50px rgba(0,0,0,0.2);
}

.family-name {
    font-size: 1.6rem;
    font-weight: 700;
    margin-top: 1rem;
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

# Header
st.markdown('<h1 class="about-title">ABOUT ME</h1>', unsafe_allow_html=True)

# Personal Information - Two Column Layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-card">
        <h2 class="info-title black-title">👤 PERSONAL INFORMATION</h2>
        <div class="info-detail">
            <strong>NAME:</strong><br>
            <span style="font-size: 1.5rem; color: #e74c3c;">QUENNIE VILLARUEL VALENZUELA</span>
        </div>
        <div class="info-detail">
            <strong>AGE:</strong><br>
            <span style="font-size: 1.5rem; color: #3498db;">21 YEARS OLD</span>
        </div>
        <div class="info-detail">
            <strong>BIRTHDATE:</strong><br>
            <span style="font-size: 1.5rem; color: #f39c12;">DECEMBER 22, 2004</span>
        </div>
        <div class="info-detail">
            <strong>STATUS:</strong><br>
            <span style="font-size: 1.5rem; color: #9b59b6;">SINGLE</span>
        </div>
        <div class="info-detail">
            <strong>ADDRESS:</strong><br>
            <span style="font-size: 1.4rem;">POBLACION EAST, MILAGROS<br>MASBATE</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h2 class="info-title black-title">🎓 EDUCATION</h2>
        <div class="info-detail">
            <strong>ELEMENTARY:</strong><br>
            MILAGROS EAST CENTRAL SCHOOL (MECS)
        </div>
        <div class="info-detail">
            <strong>HIGH SCHOOL:</strong><br>
            LICEO DE SAN JOSE INC.
        </div>
        <div class="info-detail">
            <strong>SENIOR HIGH SCHOOL:</strong><br>
            LICEO DE SAN JOSE INC.
        </div>
        <div class="info-detail">
            <strong>COLLEGE:</strong><br>
            BACHELOR OF SCIENCE IN COMPUTER SCIENCE
        </div>
        <div class="info-detail">
            <strong>TESDA CERTIFICATIONS:</strong><br>
            BOOKKEEPING NC III<br>EVENT MANAGEMENT NC III
        </div>
    </div>
    """, unsafe_allow_html=True)

# Family Section
st.markdown("""
<div class="info-card">
    <h2 class="info-title black-title">👨‍👩‍👧‍👦 FAMILY</h2>
    <div class="family-grid">
        <div class="family-card">
            <div style="font-size: 2.5rem; margin-bottom: 1rem;">👩‍🍼</div>
            <h3 style="color: #2c3e50; margin-bottom: 0.5rem;">MOTHER</h3>
            <div class="family-name" style="color: #e74c3c;">ARLENE VALENZUELA</div>
        </div>
        <div class="family-card">
            <div style="font-size: 2.5rem; margin-bottom: 1rem;">👨‍🍼</div>
            <h3 style="color: #2c3e50; margin-bottom: 0.5rem;">FATHER</h3>
            <div class="family-name" style="color: #3498db;">ENRICO VALENZUELA</div>
        </div>
        <div class="family-card">
            <div style="font-size: 2.5rem; margin-bottom: 1rem;">👦</div>
            <h3 style="color: #2c3e50; margin-bottom: 0.5rem;">BROTHER</h3>
            <div class="family-name" style="color: #f39c12;">CARL VALENZUELA</div>
        </div>
        <div class="family-card">
            <div style="font-size: 2.5rem; margin-bottom: 1rem;">👧</div>
            <h3 style="color: #2c3e50; margin-bottom: 0.5rem;">SISTER</h3>
            <div class="family-name" style="color: #9b59b6;">ERICA VALENZUELA</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Navigation Buttons (Fixed - No switch_page)
st.markdown("""
<div class="nav-buttons">
    <button class="nav-btn" onclick="window.location.href='Home.py'">🏠 HOME</button>
    <button class="nav-btn" onclick="window.location.href='pages/3_🎯_Contact.py'">🎯 CONTACT</button>
    <button class="nav-btn" onclick="window.location.href='pages/4_🛠️_Skills.py'">🛠️ SKILLS</button>
    <button class="nav-btn" onclick="window.location.href='pages/5_❓_FAQ.py'">❓ FAQ</button>
</div>
""", unsafe_allow_html=True)

# Sidebar for easy navigation
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <div style="font-size: 3rem;">👑</div>
        <h3 style="color: #2c3e50;">QUENNIE V. VALENZUELA</h3>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.current_page = "home"
        st.rerun()