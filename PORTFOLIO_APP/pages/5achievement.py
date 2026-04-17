import streamlit as st
import time

st.set_page_config(page_title="School Excellence", layout="wide")

# SAME GOLDEN DESIGN as Achievements.py - ENHANCED!
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;900&display=swap');
.main { 
    background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 30%, #a8edea 70%, #ffd89b 100%);
    min-height: 100vh;
    padding: 3rem 2rem;
}
.excellence-title {
    font-size: 5rem;
    font-weight: 900;
    background: linear-gradient(135deg, #ffd700 0%, #ff6b6b 33%, #00d2d3 66%, #ffd93d 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-bottom: 3.5rem;
    line-height: 1;
    text-shadow: 0 0 50px rgba(255,255,255,1);
    animation: titleGlow 3s ease-in-out infinite alternate;
}
@keyframes titleGlow {
    from { filter: drop-shadow(0 0 20px rgba(255,215,0,0.8)); }
    to { filter: drop-shadow(0 0 40px rgba(255,215,0,1)); }
}
.excellence-card {
    background: rgba(255,255,255,0.98);
    backdrop-filter: blur(35px);
    border-radius: 35px;
    padding: 4rem;
    margin: 3rem 0;
    box-shadow: 0 40px 100px rgba(0,0,0,0.3);
    border: 4px solid rgba(255,255,255,0.6);
    transition: all 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    position: relative;
    overflow: hidden;
}
.excellence-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 10px;
    background: linear-gradient(90deg, #ffd700, #ff6b6b, #00d2d3, #ffd93d, #6bcf7f);
    box-shadow: 0 0 20px rgba(255,215,0,0.8);
}
.excellence-card:hover {
    transform: translateY(-20px) scale(1.04);
    box-shadow: 0 70px 150px rgba(0,0,0,0.4);
    border-color: #ffd700;
}
.medal-icon {
    font-size: 6rem;
    display: block;
    text-align: center;
    margin-bottom: 2.5rem;
    animation: medalSpin 4s linear infinite;
}
@keyframes medalSpin {
    0% { transform: rotateY(0deg); }
    100% { transform: rotateY(360deg); }
}
.card-title {
    font-size: 3rem;
    font-weight: 900;
    margin-bottom: 2rem;
    text-align: center;
    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #ff6b6b 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    padding-bottom: 1.5rem;
    border-bottom: 6px solid #ffd700;
    letter-spacing: 2px;
}
.award-list {
    font-size: 1.6rem;
    color: #2c3e50;
    font-weight: 700;
    line-height: 2.2;
    text-align: center;
    margin: 2.5rem 0;
}
.award-item {
    background: linear-gradient(135deg, #fff3cd, #ffeaa7);
    margin: 1rem 0;
    padding: 1.5rem 2rem;
    border-radius: 20px;
    border-left: 8px solid #ffd700;
    box-shadow: 0 10px 30px rgba(255,215,0,0.3);
    font-size: 1.5rem;
    transition: all 0.3s ease;
}
.award-item:hover {
    transform: translateX(15px);
    box-shadow: 0 15px 40px rgba(255,215,0,0.5);
}
.legendary-highlight {
    font-size: 2.2rem;
    color: #e74c3c;
    font-weight: 900;
    text-align: center;
    margin: 3rem 0;
    background: linear-gradient(135deg, #ffd700, #ff6b6b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    padding: 2.5rem;
    border-radius: 30px;
    border: 5px solid #ffd700;
    box-shadow: 0 25px 60px rgba(255,215,0,0.6);
}
.haha-section {
    background: linear-gradient(135deg, #ff9ff3, #f368e0) !important;
    border: 4px solid #ff6b9d !important;
}
.haha-section .card-title {
    background: linear-gradient(135deg, #ffffff, #ffd700) !important;
}
.college-section {
    background: linear-gradient(135deg, #00d2d3, #6bcf7f) !important;
    color: white !important;
    border: 4px solid #00d2d3 !important;
}
.college-section .award-item {
    background: rgba(255,255,255,0.3) !important;
    color: white !important;
    border-left-color: #ffd700 !important;
}
.achievement-counter {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 2rem;
    margin: 4rem 0;
}
.counter-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 28px;
    padding: 3rem 2rem;
    text-align: center;
    box-shadow: 0 30px 80px rgba(0,0,0,0.4);
    position: relative;
    overflow: hidden;
}
.counter-number {
    font-size: 4rem;
    font-weight: 900;
    margin-bottom: 1rem;
    background: linear-gradient(135deg, #ffd700, #ffffff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.nav-buttons {
    display: flex;
    gap: 2rem;
    justify-content: center;
    margin-top: 5rem;
    flex-wrap: wrap;
}
.nav-btn {
    background: linear-gradient(135deg, #ffd700 0%, #ff6b6b 50%, #00d2d3 100%);
    color: white;
    border: none;
    border-radius: 30px;
    padding: 1.8rem 3.5rem;
    font-weight: 900;
    font-size: 1.3rem;
    cursor: pointer;
    transition: all 0.5s ease;
    text-decoration: none;
    box-shadow: 0 20px 50px rgba(0,0,0,0.4);
    letter-spacing: 2px;
    text-transform: uppercase;
}
.nav-btn:hover {
    transform: translateY(-10px) scale(1.1);
    box-shadow: 0 35px 80px rgba(255,107,107,0.7);
}
</style>
""", unsafe_allow_html=True)

# 🎖️ HERO TITLE
st.markdown("""
<div style="text-align: center; margin-bottom: 2rem;">
    <div style="font-size: 8rem; animation: bounce 2s infinite;">🎓</div>
</div>
<h1 class="excellence-title">ACADEMIC EXCELLENCE JOURNEY</h1>
<div style="text-align: center; font-size: 2rem; color: #2c3e50; font-weight: 800; margin-bottom: 4rem; max-width: 900px; margin-left: auto; margin-right: auto;">
    FROM TOP 5 TO GIN LIST - 15 YEARS OF NON-STOP WINS! 👑
</div>
""", unsafe_allow_html=True)

# 🏫 ELEMENTARY DOMINATION
st.markdown("""
<div class="excellence-card">
    <div class="medal-icon">🏫🥇</div>
    <h2 class="card-title">ELEMENTARY SCHOOL LEGEND</h2>
    <div class="award-list">
        <div class="award-item">📊 <strong>GRADE 2: TOP 5</strong></div>
        <div class="award-item">🌟 <strong>GRADE 3: BEST IN HEKASI + BEST IN FILIPINO + TOP 7</strong></div>
        <div class="award-item">📚 <strong>GRADE 4: TOP 7 + BEST IN ENGLISH</strong></div>
        <div class="award-item">⭐ <strong>GRADE 5: TOP 9</strong></div>
        <div class="award-item">🧪 <strong>GRADE 6: BEST IN SCIENCE + CONDUCT AWARD + CAMPUS JOURNALISM</strong></div>
    </div>
    <div class="legendary-highlight">
        🔥 ELEMENTARY = TOTAL DOMINATION! 10+ AWARDS! 🏆
    </div>
</div>
""", unsafe_allow_html=True)

# 🎓 HIGH SCHOOL + SENIOR HIGH
st.markdown("""
<div class="excellence-card haha-section">
    <div class="medal-icon">🎓😂</div>
    <h2 class="card-title">HIGH SCHOOL REALITY CHECK</h2>
    <div class="award-list">
        <div class="award-item">🥈 <strong>GRADE 7: WITH HIGH HONOR</strong></div>
        <div class="award-item">🥉 <strong>GRADE 8: WITH HONOR</strong></div>
        <div class="award-item">🥉 <strong>GRADE 9: WITH HONOR</strong></div>
        <div class="award-item" style="background: linear-gradient(135deg, #ff7675, #fd79a8); color: white; border-left-color: #ff6b9d;">
            😅 <strong>GRADE 10-G12: BUHAY NALANG! HAHA</strong>
        </div>
    </div>
    <div class="legendary-highlight" style="color: white; background: linear-gradient(135deg, #ff6b9d, #ff7675); border-color: #ff6b9d;">
        😂 LIFE GOT REAL BUT SURVIVED LIKE A QUEEN! 💪👑
    </div>
</div>
""", unsafe_allow_html=True)

# 🎓 COLLEGE DEAN'S LIST
st.markdown("""
<div class="excellence-card college-section">
    <div class="medal-icon">🎓📜</div>
    <h2 class="card-title">COLLEGE GIN'S LIST QUEEN</h2>
    <div class="award-list">
        <div class="award-item">📜 <strong>1ST YEAR COLLEGE: GIN LISTER</strong></div>
        <div class="award-item">📜 <strong>2ND YEAR COLLEGE: GIN LISTER</strong></div>
        <div class="award-item">📜 <strong>3RD YEAR COLLEGE: GIN LISTER</strong></div>
    </div>
    <div class="legendary-highlight" style="color: white; background: linear-gradient(135deg, #00d2d3, #6bcf7f); border-color: #ffd700;">
        🎯 3 YEARS STRAIGHT DEAN'S LIST! COLLEGE LEVEL = QUEEN LEVEL! 👑
    </div>
</div>
""", unsafe_allow_html=True)

# 📊 TOTAL ACHIEVEMENT COUNTER
st.markdown("""
<div class="achievement-counter">
    <div class="counter-card">
        <div class="counter-number">15+</div>
        <div style="font-size: 1.4rem; font-weight: 700;">Years of Excellence</div>
    </div>
    <div class="counter-card">
        <div class="counter-number">20+</div>
        <div style="font-size: 1.4rem; font-weight: 700;">Total Awards</div>
    </div>
    <div class="counter-card">
        <div class="counter-number">TOP</div>
        <div style="font-size: 1.4rem; font-weight: 700;">Consistent Rankings</div>
    </div>
    <div class="counter-card">
        <div class="counter-number">👑</div>
        <div style="font-size: 1.4rem; font-weight: 700;">Academic Queen</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Navigation Buttons
st.markdown("""
<div class="nav-buttons">
    <button class="nav-btn" onclick="window.location.href='Home.py'">🏠 HOME</button>
    <button class="nav-btn" onclick="window.location.href='pages/6_🏆_Achievements.py'">🥇 SINGLE AWARDS</button>
    <button class="nav-btn" onclick="window.location.href='pages/2_👤_About.py'">👤 ABOUT ME</button>
    <button class="nav-btn" onclick="window.location.href='pages/4_🛠️_Skills.py'">🛠️ MY SKILLS</button>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 3.5rem; background: linear-gradient(135deg, #ffd700, #ff6b6b, #00d2d3); border-radius: 35px; margin: 1rem;">
        <div style="font-size: 5rem;">🎓</div>
        <h3 style="color: white; font-weight: 900; margin-bottom: 1rem; font-size: 1.6rem;">ACADEMIC JOURNEY</h3>
        <p style="color: #fff; font-size: 1.3rem; font-weight: 800; margin-bottom: 1rem;">20+ Awards | 15 Years</p>
        <div style="font-size: 2.5rem;">👑 QUEEN 👑</div>
    </div>
    """, unsafe_allow_html=True)