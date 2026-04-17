import streamlit as st
import time

st.set_page_config(page_title="Skills", layout="wide")

# Custom CSS - Same design as Contact page
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
.main { 
    background: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 50%, #fbc2eb 100%);
    min-height: 100vh;
    padding: 3rem 2rem;
}
.skills-title {
    font-size: 4.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-bottom: 3rem;
}
.skill-card {
    background: rgba(255,255,255,0.95);
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 3rem;
    margin: 2rem 0;
    box-shadow: 0 25px 50px rgba(0,0,0,0.15);
    border: 1px solid rgba(255,255,255,0.3);
    transition: all 0.3s ease;
    height: 100%;
}
.skill-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 35px 70px rgba(0,0,0,0.2);
}
.skill-card.game-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}
.skill-card.game-card .skill-description {
    color: #f0f0f0;
}
.game-card .stSelectbox > label {
    color: white !important;
    font-weight: 600;
}
.game-card .stTextInput > label {
    color: white !important;
    font-weight: 600;
}
.game-card .stSelectbox > div > div > select {
    background: linear-gradient(135deg, #00ff88, #00cc6a) !important;
    color: #000 !important;
    font-weight: 600;
    border-radius: 12px;
    border: none;
    padding: 0.8rem;
}
.game-card .stTextInput > div > div > input {
    background: white !important;
    border: 2px solid #00ff88 !important;
    border-radius: 12px;
    padding: 0.8rem;
    font-weight: 600;
}
.skill-icon {
    font-size: 4rem;
    display: block;
    text-align: center;
    margin-bottom: 1.5rem;
}
.skill-title {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 1.5rem;
    text-align: center;
    padding-bottom: 1rem;
    border-bottom: 3px solid #3498db;
}
.skill-title.black-title {
    color: #000000 !important;
}
.skill-title.game-title {
    color: #ffffff !important;
    border-bottom: 3px solid #00ff88;
}
.skill-description {
    font-size: 1.2rem;
    color: #34495e;
    line-height: 1.8;
    text-align: justify;
}
.skill-highlight {
    font-size: 1.3rem;
    color: #e74c3c;
    font-weight: 600;
}
.game-highlight {
    color: #00ff88 !important;
    font-weight: 700;
}
.game-instruction {
    background: rgba(0,255,136,0.3);
    border-radius: 12px;
    padding: 1.5rem;
    margin-top: 1.5rem;
    border-left: 5px solid #00ff88;
    text-align: center;
    font-weight: 600;
    color: #000;
}
.success-game {
    background: linear-gradient(135deg, #00ff88, #00cc6a);
    color: #000;
    padding: 1.5rem;
    border-radius: 16px;
    text-align: center;
    font-weight: 700;
    font-size: 1.2rem;
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

# Main Title
st.markdown('<h1 class="skills-title">🛠️ MY SKILLS</h1>', unsafe_allow_html=True)

# Skills Grid - Row 1 (Writing Skills with BLACK titles)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="skill-card">
        <div class="skill-icon">📖</div>
        <h2 class="skill-title black-title">WRITING STORIES</h2>
        <div class="skill-description">
            Since I was a kid, I <span class="skill-highlight">really really loved to write stories</span> 
            especially in a <strong>horror</strong> and <strong>romantic</strong> genre. 
            The reason behind that is because I also love reading up until now. 
            My favorite platforms are <strong>eBook</strong> and <strong>Wattpad</strong>! ✨
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="skill-card">
        <div class="skill-icon">✍️</div>
        <h2 class="skill-title black-title">MAKING POEMS & ESSAYS</h2>
        <div class="skill-description">
            When I was in <strong>elementary</strong>, I joined <strong>campus journalism</strong> 
            and even got an <span class="skill-highlight">award for it</span> when I graduated! 
            In high school, I also joined an <strong>essay competition</strong>.
            <br><br>
            Teachers said a G12 student would win (I was Grade 9), but 
            <strong>GUESS WHAT? YES I WON! 😎</strong> (Didn't attend ceremony though!)
        </div>
    </div>
    """, unsafe_allow_html=True)

# Gaming Skills - Full Width Special Card
st.markdown("""
<div class="skill-card game-card">
    <div class="skill-icon">🎮</div>
    <h2 class="skill-title game-title">GAMING PRO 🎯</h2>
    <div class="skill-description">
        I also play different <span class="game-highlight">online games</span> like:
        <strong>Rules of Survival (ROS)</strong>, <strong>Mobile Legends</strong>, 
        <strong>CODM</strong>, <strong>Valorant</strong>, and <strong>League of Legends</strong>!
        <br><br>
        There was a time I was <span class="game-highlight">so addicted to ROS</span> at the computer shop! 
        I was the <strong>ONLY GIRL</strong> joining many events. We had a <strong>clan master from Japan</strong> 
        who gave us prizes whenever we won! He even brought <strong>jerseys for our clan</strong> 
        and I was <span class="game-highlight">so lucky to get a free one! 🏆</span>
    </div>
    """, unsafe_allow_html=True)

# Clear Instruction
st.markdown("""
    <div class="game-instruction">
        🎮 <strong>Choose a game you like, drop your ID, and let's add each other as friends!</strong> 👑
    </div>
    """, unsafe_allow_html=True)

# FIXED Interactive Gaming Form (REMOVED css_class)
with st.form("game_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    
    with col1:
        selected_game = st.selectbox(
            "🎯 Choose Game:",
            ["Rules of Survival (ROS)", "Mobile Legends", "CODM", "Valorant", "League of Legends"]
        )
    
    with col2:
        player_id = st.text_input("🆔 Your Player ID:", placeholder="Enter your ID...")
    
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        submit_game = st.form_submit_button("🤝 ADD FRIEND!", use_container_width=True)
    
    if submit_game and player_id:
        st.success(f"✅ **{selected_game} Friend Added!** 🎉\n**ID:** `{player_id}`\n**See you in game!** 👑🎮")
        st.balloons()
        time.sleep(2)
        st.rerun()
    elif submit_game:
        st.warning("❌ Please enter your Player ID to add friend!")

st.markdown("</div>", unsafe_allow_html=True)

# Special Note Section
st.markdown("""
<div class="skill-card" style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);">
    <div class="skill-icon">💭</div>
    <h2 class="skill-title black-title">MY MULTI-TALENTED SIDE</h2>
    <div class="skill-description">
        From <strong>writing epic stories</strong> to <strong>dominating in gaming tournaments</strong>, 
        I'm a creative soul with competitive fire! Whether it's words or wins, 
        I give my all! 🔥📝🎮
    </div>
</div>
""", unsafe_allow_html=True)

# Navigation Buttons
st.markdown("""
<div class="nav-buttons">
    <button class="nav-btn" onclick="window.location.href='Home.py'">🏠 HOME</button>
    <button class="nav-btn" onclick="window.location.href='pages/2_👤_About.py'">👤 ABOUT</button>
    <button class="nav-btn" onclick="window.location.href='pages/3_🎯_Contact.py'">🎯 CONTACT</button>
    <button class="nav-btn" onclick="window.location.href='pages/5_❓_FAQ.py'">❓ FAQ</button>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <div style="font-size: 3rem;">👑</div>
        <h3 style="color: #2c3e50;">QUENNIE V. VALENZUELA</h3>
        <p style="color: #7f8c8d; font-size: 0.9rem;">Writer × Gamer × Champion ✨🎮</p>
    </div>
    """, unsafe_allow_html=True)