import streamlit as st

st.set_page_config(
    page_title="RADIA AI | Radiology Academy",
    page_icon="🩻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- DESIGN ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #081421;
    color: #F2F7FA;
}

.block-container {
    max-width: 1050px;
    padding: 2rem 1.3rem 4rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

#MainMenu, footer {
    visibility: hidden;
}

.hero {
    background: linear-gradient(120deg, #102D40, #13566A);
    border: 1px solid #26758A;
    border-radius: 24px;
    padding: 30px 25px;
    margin: 15px 0 28px;
}

.eyebrow {
    color: #75E0D0;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2px;
}

.hero h1 {
    color: white;
    font-size: clamp(32px, 6vw, 48px);
    line-height: 1.12;
    margin: 12px 0;
    font-weight: 800;
}

.hero p {
    color: #D0E5EC;
    font-size: 16px;
    max-width: 570px;
    line-height: 1.6;
}

.section-title {
    color: #F2F7FA;
    font-size: 23px;
    font-weight: 800;
    margin: 28px 0 12px;
}

.section-sub {
    color: #91A8B8;
    font-size: 14px;
    margin-top: -7px;
    margin-bottom: 18px;
}

.feature-card {
    background: #122436;
    border: 1px solid #28465A;
    border-radius: 18px;
    padding: 20px;
    min-height: 150px;
    margin-bottom: 12px;
}

.feature-card h3 {
    color: #FFFFFF;
    font-size: 18px;
    margin: 8px 0;
}

.feature-card p {
    color: #AFC2CF;
    font-size: 13px;
    line-height: 1.5;
}

.icon {
    font-size: 27px;
}

.case-card {
    background: #102335;
    border: 1px solid #29475A;
    border-radius: 16px;
    padding: 17px;
    margin-bottom: 12px;
}

.case-tag {
    color: #72DCCB;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1px;
}

.case-card h4 {
    color: white;
    margin: 8px 0;
    font-size: 17px;
}

.case-card p {
    color: #AFC2CF;
    font-size: 13px;
}

.footer {
    text-align: center;
    color: #71899A;
    font-size: 12px;
    padding-top: 30px;
}

.stButton > button {
    background: linear-gradient(90deg, #19A995, #32C5B2);
    color: #061B23;
    border: none;
    border-radius: 12px;
    font-weight: 800;
    min-height: 45px;
    width: 100%;
}

.stButton > button:hover {
    background: #70E2D0;
    color: #061B23;
    border: none;
}

div[data-testid="stMetric"] {
    background: #122436;
    border: 1px solid #28465A;
    padding: 14px;
    border-radius: 14px;
}

div[data-testid="stMetricLabel"] {
    color: #AFC2CF;
}

div[data-testid="stMetricValue"] {
    color: #75E0D0;
}

.stRadio label {
    color: #E7F1F5 !important;
}
</style>
""", unsafe_allow_html=True)


# ---------- NAVIGATION ----------
if "page" not in st.session_state:
    st.session_state.page = "Home"

st.markdown("""
<div style="display:flex;align-items:center;gap:12px;">
    <div style="font-size:38px;">🩻</div>
    <div>
        <div style="font-size:25px;font-weight:800;letter-spacing:1px;">
            RADIA <span style="color:#55D4C2;">AI</span>
        </div>
        <div style="font-size:11px;color:#91A8B8;letter-spacing:2px;">
            SEE • UNDERSTAND • LEARN
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")

pages = ["Home", "Case Library", "My Learning"]
selected = st.radio(
    "Navigation",
    pages,
    horizontal=True,
    label_visibility="collapsed",
    index=pages.index(st.session_state.page)
)
st.session_state.page = selected

st.divider()


# ---------- HOME ----------
if st.session_state.page == "Home":

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">YOUR RADIOLOGY LEARNING SPACE</div>
        <h1>See beyond<br>the X-ray.</h1>
        <p>
        Build your radiology knowledge through visual cases,
        guided explanations and interactive learning.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Your learning dashboard</div>',
                unsafe_allow_html=True)

    m1, m2 = st.columns(2)
    with m1:
        st.metric("Learning modules", "01", "Starting with chest X-ray")
    with m2:
        st.metric("Your progress", "0%", "Your journey starts here")

    st.markdown('<div class="section-title">Explore learning</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Choose where you want to begin.</div>',
                unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
        <div class="feature-card">
            <div class="icon">🫁</div>
            <h3>Chest X-ray</h3>
            <p>Learn chest anatomy, image patterns and systematic interpretation.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Explore chest X-ray", key="chest"):
            st.session_state.page = "Case Library"
            st.rerun()

    with c2:
        st.markdown("""
        <div class="feature-card">
            <div class="icon">🧠</div>
            <h3>Knowledge check</h3>
            <p>Test your understanding with case-based learning questions.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View learning area", key="quiz"):
            st.session_state.page = "My Learning"
            st.rerun()

    st.markdown('<div class="section-title">Featured learning path</div>',
                unsafe_allow_html=True)

    st.markdown("""
    <div class="case-card">
        <div class="case-tag">BEGINNER • MODULE 01</div>
        <h4>Introduction to Chest Radiography</h4>
        <p>Start with image orientation, normal anatomy and a systematic approach.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open learning path"):
        st.session_state.page = "Case Library"
        st.rerun()


# ---------- CASE LIBRARY ----------
elif st.session_state.page == "Case Library":

    st.markdown('<div class="section-title">Chest X-ray Library</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Your visual radiology classroom.</div>',
                unsafe_allow_html=True)

    st.info("Our educational case collection is being prepared.")

    cases = [
        ("01", "Normal Chest Anatomy", "Beginner", "Recognise the major structures."),
        ("02", "Understanding Chest Views", "Beginner", "Explore common radiographic views."),
        ("03", "Systematic Image Review", "Beginner", "Learn a structured examination approach."),
    ]

    for number, title, level, description in cases:
        st.markdown(f"""
        <div class="case-card">
            <div class="case-tag">CASE {number} • {level.upper()}</div>
            <h4>{title}</h4>
            <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)

    st.caption("These are planned learning modules, not completed diagnostic cases.")


# ---------- MY LEARNING ----------
elif st.session_state.page == "My Learning":

    st.markdown('<div class="section-title">My Learning</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Track your journey with RADIA Academy.</div>',
                unsafe_allow_html=True)

    st.metric("Cases completed", "0")
    st.metric("Quiz score", "Not attempted")

    st.markdown("""
    <div class="feature-card">
        <div class="icon">📚</div>
        <h3>Your study journey starts here</h3>
        <p>
        Complete learning cases and quizzes to build your personal
        revision record. Progress tracking will expand in future versions.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Browse learning cases"):
        st.session_state.page = "Case Library"
        st.rerun()
# ------------ FOOTER ------------
st.markdown("""
<div class="footer">
    RADIA AI • RADIA ACADEMY<br>
    Founded & Developed by<br>
    <span style="
        color:#75E0D0;
        font-size:15px;
        font-weight:800;
        letter-spacing:0.5px;">
        Dr. H. Azib Abdullah Khan
    </span>
    <br><br>
    Learning support only • Not a diagnostic tool
</div>
""", unsafe_allow_html=True)
