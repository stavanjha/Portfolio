import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Stavan Jha | Software Engineer",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"

# Visual styling is embedded here so the project remains Python-only.
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&display=swap');
:root { --ink:#171717; --muted:#66645f; --paper:#f6f5f0; --lime:#d8ff3e; --line:#deddd5; }
html, body, [class*="css"] { font-family:'Manrope', sans-serif; color:var(--ink); }
.stApp { background:var(--paper); }
header[data-testid="stHeader"] { background:transparent; }
.block-container { max-width:1180px; padding-top:1.3rem; padding-bottom:4rem; }
#MainMenu, footer {visibility:hidden;}
div[data-testid="stToolbar"] {visibility:hidden; height:0;}
.nav { display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--line); padding:0 0 18px; margin-bottom:52px; }
.brand {font-weight:800; letter-spacing:-1px; font-size:20px;}
.brand span {background:var(--lime); border-radius:50%; display:inline-block; width:9px;height:9px;margin-left:4px;}
.navright {font-family:'DM Mono',monospace;font-size:11px;letter-spacing:1px;color:#555;}
.eyebrow {font-family:'DM Mono',monospace; font-size:11px; letter-spacing:1.8px; text-transform:uppercase; color:#666; margin-bottom:16px;}
.hero-title {font-size:clamp(42px,6.5vw,82px); line-height:.99; letter-spacing:-5px; font-weight:800; margin:0 0 25px;}
.hero-title .outline {color:transparent;-webkit-text-stroke:1.5px #202020;}
.hero-copy {font-size:17px;line-height:1.8;color:#5f5e59;max-width:570px;}
.pill {display:inline-block;border:1px solid #c8c7bf;border-radius:40px;padding:8px 13px;font-family:'DM Mono',monospace;font-size:10px;letter-spacing:.8px;margin:4px 4px 0 0;}
.section-head {display:flex;justify-content:space-between;align-items:end;border-bottom:1px solid var(--line);padding-bottom:16px;margin:68px 0 25px;}
.section-head h2 {font-size:34px;letter-spacing:-1.7px;font-weight:800;margin:0;}
.section-head p {font-family:'DM Mono',monospace;font-size:10px;letter-spacing:1px;color:#777;margin:0;}
.project {background:#fff;border:1px solid #e7e6df;border-radius:18px;padding:25px 25px 22px;min-height:300px;display:flex;flex-direction:column;justify-content:space-between;margin-bottom:14px;}
.project .num {font-family:'DM Mono',monospace;font-size:11px;color:#888;}
.project h3 {font-size:26px;line-height:1.15;letter-spacing:-1px;margin:23px 0 12px;font-weight:800;}
.project p {font-size:14px;line-height:1.75;color:#64635e;}
.tags {font-family:'DM Mono',monospace;font-size:10px;color:#555;line-height:2;}
.highlight {background:var(--lime);border-radius:16px;padding:25px 26px;margin:10px 0 20px;}
.highlight h3 {font-size:25px;letter-spacing:-1px;margin:0 0 10px;}
.small-label {font-family:'DM Mono',monospace;text-transform:uppercase;font-size:10px;letter-spacing:1.5px;}
.skillbox {border-top:1px solid var(--line);padding:17px 0;}
.skillbox h4 {font-size:15px;margin:0 0 9px;font-weight:800;}
.skillbox p {color:#64635e;font-size:13px;line-height:1.8;margin:0;}
.timeline {border-left:1px solid #ccc;padding:0 0 25px 22px;position:relative;}
.timeline:before {content:'';width:8px;height:8px;background:var(--lime);border:1px solid #222;border-radius:50%;position:absolute;left:-5px;top:5px;}
.timeline h3 {font-size:18px;margin:0 0 6px;letter-spacing:-.4px;}
.timeline p {font-size:13px;line-height:1.75;color:#666;margin:0;}
.contact {background:#191919;color:#f6f5f0;border-radius:22px;padding:35px;}
.contact h2 {font-size:clamp(35px,5vw,58px);line-height:1.02;letter-spacing:-3px;margin:12px 0 20px;}
.contact p {color:#c3c2bc;line-height:1.8;}
.contact a {color:#d8ff3e;text-decoration:none;}
a {color:#171717;}
div.stButton > button {border-radius:40px;border:1px solid #222;background:#191919;color:white;padding:10px 20px;font-weight:700;}
div.stButton > button:hover {background:var(--lime);color:#171717;border-color:#171717;}
div[data-testid="stImage"] img {border-radius:18px;object-fit:cover;}
@media(max-width:700px){.hero-title{letter-spacing:-2.5px}.nav{margin-bottom:30px}.section-head{margin-top:45px}.project{min-height:250px}}
</style>
""", unsafe_allow_html=True)

def section(title, index):
    st.markdown(f'<div class="section-head"><h2>{title}</h2><p>{index} / SELECTED WORK</p></div>', unsafe_allow_html=True)

# Navigation
st.markdown("""
<div class="nav">
  <div class="brand">SJ<span></span></div>
  <div class="navright">SOFTWARE · AI/ML · SECURITY</div>
</div>
""", unsafe_allow_html=True)

left, right = st.columns([1.35, .75], gap="large", vertical_alignment="center")
with left:
    st.markdown('<div class="eyebrow">PORTFOLIO / 2026 — FARIDABAD, INDIA</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="hero-title">Stavan<br>Jha<span class="outline">.</span></h1>', unsafe_allow_html=True)
    st.markdown('<div class="eyebrow">ASPIRING SOFTWARE ENGINEER · AI/ML ENTHUSIAST</div>', unsafe_allow_html=True)
    st.markdown('<p class="hero-copy">I build practical software at the intersection of intelligent systems, application security, and thoughtful user experiences. Currently pursuing Computer Science Engineering and looking for opportunities to contribute to real-world software.</p>', unsafe_allow_html=True)
    st.markdown('<span class="pill">PYTHON</span><span class="pill">AI / ML</span><span class="pill">CYBERSECURITY</span><span class="pill">ANDROID</span>', unsafe_allow_html=True)
    st.write("")
    c1, c2 = st.columns([1, 1])
    with c1:
        if st.button("Explore my work ↘", use_container_width=True):
            st.session_state["show_work_note"] = True
    with c2:
        st.link_button("GitHub ↗", "https://github.com/stavanjha", use_container_width=True)
    if st.session_state.get("show_work_note"):
        st.info("Scroll to Selected Work to explore the projects featured in my resume.")
with right:
    st.image(str(ASSETS / "stavan.jpg"), use_container_width=True)
    st.markdown('<div class="small-label" style="margin-top:10px;">BUILD WITH PURPOSE. LEARN BY SHIPPING.</div>', unsafe_allow_html=True)

section("Selected work", "01")
st.markdown('<p style="color:#686760;max-width:650px;line-height:1.8;">A selection of projects focused on security, applied machine learning, and useful software experiences.</p>', unsafe_allow_html=True)

p1, p2 = st.columns(2, gap="medium")
with p1:
    st.markdown("""
    <div class="project">
      <div><div class="num">01 / MACHINE LEARNING + SECURITY</div>
      <h3>SaferCyber</h3>
      <p>An AI-based cyber threat detection and monitoring framework built as a multi-page Streamlit application and evaluated on the CICIDS2017 network-traffic dataset.</p>
      <p>Integrated Random Forest, SVM, and XGBoost models with SHAP explainability, plus a vulnerability-scanning module and exportable PDF threat reports.</p></div>
      <div class="tags">PYTHON · STREAMLIT · SCIKIT-LEARN · SHAP · XGBOOST</div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("View repository ↗", "https://github.com/stavanjha/SaferCyber-AI-Based-Cyber-Threat-Detection-Framework-using-Random-Forest-SVM-and-XGBoost", use_container_width=True)
with p2:
    st.markdown("""
    <div class="project">
      <div><div class="num">02 / ANDROID + PRIVACY</div>
      <h3>GuardPlus</h3>
      <p>A native Android privacy-risk scanner that reviews installed applications and classifies requested permissions as Low, Medium, High, or Critical.</p>
      <p>Includes a sortable, risk-scored dashboard designed to help users identify potential privacy concerns, with local persistence for app data.</p></div>
      <div class="tags">KOTLIN · JETPACK COMPOSE · HILT · ROOM</div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("View repository ↗", "https://github.com/stavanjha/GuardPlus", use_container_width=True)

p3, p4 = st.columns(2, gap="medium")
with p3:
    st.markdown("""
    <div class="project">
      <div><div class="num">03 / MEDIA AUTHENTICITY</div>
      <h3>Fake Image &amp; Video Detector</h3>
      <p>An AI-based tool designed to assess whether images and videos may have been manipulated, combining media analysis with a user-friendly verification workflow.</p>
      <p>Presented at a college-level hackathon, where the project earned third place.</p></div>
      <div class="tags">MACHINE LEARNING · MEDIA ANALYSIS · UX</div>
    </div>
    """, unsafe_allow_html=True)
with p4:
    st.markdown("""
    <div class="highlight">
      <div class="small-label">RECOGNITION / MARCH 2026</div>
      <h3>3rd place — College Hackathon</h3>
      <p>Recognized for the Fake Image &amp; Video Detector Tool.</p>
      <hr style="border:0;border-top:1px solid #a6bf37;margin:20px 0;">
      <div class="small-label">FEBRUARY 2026</div>
      <h3>2nd place — Turbo AI Competition</h3>
      <p>Designed a Smart Traffic Signal System.</p>
    </div>
    """, unsafe_allow_html=True)

section("What I work with", "02")
s1, s2, s3 = st.columns(3, gap="large")
with s1:
    st.markdown('<div class="skillbox"><h4>Programming</h4><p>Python<br>Java · C<br>Object-Oriented Programming<br>Data Structures &amp; Algorithms</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="skillbox"><h4>Web &amp; data</h4><p>HTML · CSS · JavaScript<br>React.js<br>SQL · MySQL<br>REST APIs</p></div>', unsafe_allow_html=True)
with s2:
    st.markdown('<div class="skillbox"><h4>Machine learning</h4><p>Random Forest · SVM · XGBoost<br>Model evaluation<br>Scikit-learn · Pandas · NumPy<br>SHAP · Streamlit</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="skillbox"><h4>Android development</h4><p>Kotlin<br>Jetpack Compose<br>Hilt · Room</p></div>', unsafe_allow_html=True)
with s3:
    st.markdown('<div class="skillbox"><h4>Design &amp; engineering</h4><p>UI/UX design<br>Wireframing · Prototyping<br>Unit testing<br>System reliability · Problem solving</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="skillbox"><h4>Tools</h4><p>Git · GitHub<br>REST API integration<br>Software documentation</p></div>', unsafe_allow_html=True)

section("Education & learning", "03")
e1, e2 = st.columns([1.1, .9], gap="large")
with e1:
    st.markdown("""
    <div class="timeline">
      <div class="eyebrow">CURRENT / 3RD YEAR</div>
      <h3>B.Tech — Computer Science Engineering</h3>
      <p>Mangalmay Institute of Engineering and Technology<br>Affiliated to Dr. A.P.J. Abdul Kalam Technical University (AKTU), Lucknow</p>
      <p style="margin-top:12px;"><strong>Approx. CGPA: 8.17</strong><br>SGPA: 8.55 · 8.18 · 7.92 · 8.04 (Semesters 1–4)</p>
    </div>
    """, unsafe_allow_html=True)
with e2:
    st.markdown('<div class="eyebrow">TRAINING &amp; CERTIFICATIONS</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="timeline"><h3>Programming in Java — NPTEL</h3><p>Elite + Gold · 94% · May 2026</p></div>
    <div class="timeline"><h3>Software Engineering Job Simulation — HPE / Forage</h3><p>RESTful service, data-upload functionality, and unit testing · Jul 2026</p></div>
    <div class="timeline"><h3>Artificial Intelligence Virtual Program — IBMCEP</h3><p>IBM Developer Skills Network · Jun–Aug 2026</p></div>
    <div class="timeline"><h3>Generative AI Training — IIT Kharagpur</h3><p>Generative AI fundamentals and modern AI workflows</p></div>
    <div class="timeline"><h3>Advanced Python Programming — IIT Bombay</h3><p>Advanced Python concepts and modular programming</p></div>
    <div class="timeline"><h3>DSA Using C — RSPL Technologies</h3><p>Algorithms, optimization, and problem-solving</p></div>
    """, unsafe_allow_html=True)

section("A little about me", "04")
about_l, about_r = st.columns([1, 1], gap="large")
with about_l:
    st.markdown('<h3 style="font-size:27px;letter-spacing:-1px;">Curious by default.<br>Practical by design.</h3>', unsafe_allow_html=True)
with about_r:
    st.markdown('<p style="color:#666;line-height:1.9;">I enjoy turning technical concepts into working projects—from experimenting with machine-learning models to building Android tools that make privacy information easier to understand. I value clear documentation, reliable implementation, and learning through hands-on development.</p>', unsafe_allow_html=True)

st.markdown("""
<div class="contact">
  <div class="small-label">HAVE AN OPPORTUNITY OR A PROJECT IN MIND?</div>
  <h2>Let's build<br>something useful.</h2>
  <p>I'm seeking a Software Engineering internship and opportunities to learn from real-world engineering teams.</p>
  <p><a href="mailto:stavanjha2006@gmail.com">stavanjha2006@gmail.com</a><br>
  <a href="https://www.linkedin.com/in/stavan-jha-674908317/">LinkedIn ↗</a> &nbsp;·&nbsp;
  <a href="https://github.com/stavanjha">GitHub ↗</a></p>
  <p style="font-size:12px;margin-top:28px;">Faridabad, Haryana, India</p>
</div>
""", unsafe_allow_html=True)

st.write("")
resume_path = ASSETS / "Stavan_Jha_Resume.docx"
with open(resume_path, "rb") as resume_file:
    st.download_button(
        "Download resume (DOCX) ↓",
        data=resume_file,
        file_name="Stavan_Jha_Resume.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )
st.markdown('<p style="font-family:DM Mono,monospace;font-size:10px;color:#888;text-align:center;margin-top:28px;">© 2026 STAVAN JHA · DESIGNED & BUILT WITH PYTHON + STREAMLIT</p>', unsafe_allow_html=True)
