import streamlit as st
import asyncio
import uuid

from agents.coordinator import coordinator
from utils.response_normalizer import normalize_response

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="AI Wedding Planner",
    page_icon="💍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Hero Image
# --------------------------------------------------
# Replace this with your own image URL, or a local path via st.image-based
# encoding if you want a fully custom / offline picture.

HERO_IMAGE_URL = "https://images.unsplash.com/photo-1519225421980-715cb0215aed?q=80&w=1600&h=500&fit=crop&auto=format"

# --------------------------------------------------
# Premium CSS Styling
# --------------------------------------------------

_CSS = """
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', 'Inter', sans-serif;
}

/* Main app background - warm cream, luxury feel */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg, #FCFBF8 0%, #F9F7F4 100%);
}

[data-testid="stHeader"] {
    background: transparent;
}

/* Hide default streamlit footer/menu clutter */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* --------------------------------------------------
   Sidebar
-------------------------------------------------- */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #2B1B2F 0%, #1F1425 100%);
    color: #F5EDE6;
}

[data-testid="stSidebar"] * {
    color: #F5EDE6 !important;
}

[data-testid="stSidebar"] h1 {
    font-weight: 700;
    font-size: 1.6rem;
    padding-bottom: 0.2rem;
}

.sidebar-divider {
    border: none;
    border-top: 1px solid rgba(245, 237, 230, 0.15);
    margin: 1rem 0;
}

.sidebar-section-title {
    font-size: 0.75rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #D8A7C4 !important;
    margin-bottom: 0.4rem;
    font-weight: 600;
}

.sidebar-credit {
    font-size: 0.85rem;
    opacity: 0.85;
    line-height: 1.6;
}

.sidebar-badge {
    display: inline-block;
    background: rgba(216, 167, 196, 0.15);
    border: 1px solid rgba(216, 167, 196, 0.35);
    color: #D8A7C4 !important;
    padding: 3px 10px;
    border-radius: 20px;
    font-size: 0.72rem;
    margin: 3px 4px 3px 0;
}

/* Sidebar buttons */
[data-testid="stSidebar"] button {
    background: linear-gradient(90deg, #E786A0, #9B5DE5) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}

[data-testid="stSidebar"] button:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 16px rgba(155, 93, 229, 0.4);
}

/* --------------------------------------------------
   Hero Section
-------------------------------------------------- */
.hero-wrap {
    position: relative;
    width: 100%;
    height: 280px;
    border-radius: 20px;
    overflow: hidden;
    margin-bottom: 1.8rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.14);
    background-image:
        linear-gradient(180deg, rgba(30,15,35,0.55) 0%, rgba(30,15,35,0.72) 100%),
        url('__HERO_IMAGE_URL__');
    background-size: cover;
    background-position: center 35%;
    background-repeat: no-repeat;
}

.hero-overlay {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 0 1.5rem;
}

.hero-title {
    color: #FFFFFF;
    font-size: 2.4rem;
    font-weight: 700;
    margin: 0;
    text-shadow: 0 2px 12px rgba(0,0,0,0.35);
}

.hero-subtitle {
    color: #F3D9E6;
    font-size: 1.05rem;
    font-weight: 400;
    margin-top: 0.5rem;
    letter-spacing: 0.3px;
    text-shadow: 0 2px 8px rgba(0,0,0,0.35);
}

/* --------------------------------------------------
   Feature / Icon Cards
-------------------------------------------------- */
.feature-row {
    display: flex;
    gap: 14px;
    margin-bottom: 1.8rem;
    flex-wrap: wrap;
}

.feature-card {
    flex: 1;
    min-width: 140px;
    background: #FFFFFF;
    border-radius: 16px;
    padding: 1rem 0.8rem;
    text-align: center;
    box-shadow: 0 4px 14px rgba(155, 93, 229, 0.08);
    border: 1px solid #F0E6EC;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}

.feature-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 24px rgba(155, 93, 229, 0.18);
}

.feature-icon {
    font-size: 1.8rem;
    margin-bottom: 0.3rem;
}

.feature-label {
    font-weight: 600;
    font-size: 0.9rem;
    color: #3A2A3D;
}

/* --------------------------------------------------
   Chat Bubbles (custom-rendered, not dependent on
   Streamlit's internal chat_message DOM structure)
-------------------------------------------------- */
.chat-row {
    display: flex;
    align-items: flex-end;
    gap: 10px;
    margin-bottom: 14px;
}

.chat-row.user {
    flex-direction: row-reverse;
}

.chat-avatar {
    width: 34px;
    height: 34px;
    min-width: 34px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.1rem;
}

.chat-avatar.user {
    background: linear-gradient(135deg, #6C63FF, #9B5DE5);
}

.chat-avatar.assistant {
    background: #FDE9F0;
}

.chat-bubble {
    max-width: 72%;
    padding: 0.75rem 1.05rem;
    font-size: 0.96rem;
    line-height: 1.55;
}

.chat-bubble.user {
    background: linear-gradient(135deg, #6C63FF, #9B5DE5);
    color: #FFFFFF;
    border-radius: 18px 18px 4px 18px;
    box-shadow: 0 4px 14px rgba(108, 99, 255, 0.25);
}

.chat-bubble.user p, .chat-bubble.user * {
    color: #FFFFFF !important;
}

.chat-bubble.assistant {
    background: #FFFFFF;
    color: #3A2A3D;
    border-radius: 18px 18px 18px 4px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.06);
    border: 1px solid #F0E6EC;
}

.chat-bubble p {
    margin: 0 0 0.5rem 0;
}

.chat-bubble p:last-child {
    margin-bottom: 0;
}

.chat-bubble h1, .chat-bubble h2, .chat-bubble h3, .chat-bubble h4 {
    margin: 0.6rem 0 0.4rem 0;
    font-weight: 600;
    line-height: 1.3;
}

.chat-bubble h1 { font-size: 1.25rem; }
.chat-bubble h2 { font-size: 1.15rem; }
.chat-bubble h3 { font-size: 1.05rem; color: #9B5DE5; }
.chat-bubble h4 { font-size: 0.98rem; color: #9B5DE5; }

.chat-bubble.user h1, .chat-bubble.user h2,
.chat-bubble.user h3, .chat-bubble.user h4 {
    color: #FFFFFF !important;
}

.chat-bubble ul, .chat-bubble ol {
    margin: 0.3rem 0 0.6rem 0;
    padding-left: 1.3rem;
}

.chat-bubble li {
    margin-bottom: 0.25rem;
}

.chat-bubble strong {
    font-weight: 700;
    color: #6C3D82;
}

.chat-bubble.user strong {
    color: #FFFFFF !important;
}

.chat-bubble em {
    color: inherit;
}

.chat-bubble code {
    background: rgba(155, 93, 229, 0.1);
    padding: 1px 6px;
    border-radius: 5px;
    font-size: 0.85em;
}

.chat-bubble table {
    border-collapse: collapse;
    margin: 0.5rem 0;
    width: 100%;
    font-size: 0.9rem;
}

.chat-bubble th, .chat-bubble td {
    border: 1px solid #EADDE6;
    padding: 6px 10px;
    text-align: left;
}

.chat-bubble th {
    background: #FBF3F8;
}

.chat-bubble hr {
    border: none;
    border-top: 1px solid #EADDE6;
    margin: 0.6rem 0;
}

/* --------------------------------------------------
   Chat input box (bottom fixed area)
-------------------------------------------------- */
[data-testid="stBottomBlockContainer"],
[data-testid="stBottom"] > div {
    background: linear-gradient(180deg, rgba(249,247,244,0) 0%, #F9F7F4 40%) !important;
}

[data-testid="stChatInput"] {
    background: transparent !important;
}

[data-testid="stChatInput"] > div {
    background: #FFFFFF !important;
    border: 1px solid #E8D5DE !important;
    border-radius: 26px !important;
    box-shadow: 0 6px 20px rgba(155, 93, 229, 0.12) !important;
    padding: 2px 6px !important;
}

[data-testid="stChatInput"] > div:focus-within {
    border: 1px solid #9B5DE5 !important;
    box-shadow: 0 6px 20px rgba(155, 93, 229, 0.22) !important;
}

[data-testid="stChatInput"] textarea {
    border: none !important;
    box-shadow: none !important;
    font-family: 'Poppins', 'Inter', sans-serif !important;
    color: #3A2A3D !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #B8A6B5 !important;
}

/* Send button */
[data-testid="stChatInput"] button {
    background: linear-gradient(135deg, #6C63FF, #9B5DE5) !important;
    border-radius: 50% !important;
    border: none !important;
}

[data-testid="stChatInput"] button svg {
    fill: #FFFFFF !important;
}

/* --------------------------------------------------
   Footer
-------------------------------------------------- */
.app-footer {
    text-align: center;
    margin-top: 2.5rem;
    padding-top: 1.2rem;
    border-top: 1px solid #EDE2E8;
    color: #8A7A8C;
    font-size: 0.85rem;
    line-height: 1.7;
}

.app-footer b {
    color: #6C5B6E;
}

</style>
"""

st.markdown(_CSS.replace("__HERO_IMAGE_URL__", HERO_IMAGE_URL), unsafe_allow_html=True)

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.title("💍 AI Wedding Planner")

    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-section-title">Session</div>', unsafe_allow_html=True)
    st.code(st.session_state.thread_id[:8])

    if st.button("🆕 New Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.thread_id = str(uuid.uuid4())
        st.rerun()

    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-section-title">About Project</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="sidebar-credit">
        An AI-powered wedding planning assistant that helps you plan venue,
        budget, catering, decoration and timeline — all through a
        conversational multi-agent system.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-section-title">Developed By</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-credit">👨‍💻 <b>Wakeel Ahmad</b></div>', unsafe_allow_html=True)

    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-section-title">Powered By</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <span class="sidebar-badge">LangChain</span>
        <span class="sidebar-badge">Azure OpenAI</span>
        <span class="sidebar-badge">Streamlit</span>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# Hero Section
# --------------------------------------------------

st.markdown(
    """
    <div class="hero-wrap">
        <div class="hero-overlay">
            <div class="hero-title">💍 AI Wedding Planner</div>
            <div class="hero-subtitle">Plan Your Dream Wedding — Powered by LangChain AI Agents</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Feature Cards
# --------------------------------------------------

st.markdown(
    """
    <div class="feature-row">
        <div class="feature-card">
            <div class="feature-icon">🏛</div>
            <div class="feature-label">Venue</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">💰</div>
            <div class="feature-label">Budget</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🍽</div>
            <div class="feature-label">Catering</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🌸</div>
            <div class="feature-label">Decoration</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🕒</div>
            <div class="feature-label">Timeline</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# LangGraph Config
# --------------------------------------------------

config = {
    "configurable": {
        "thread_id": st.session_state.thread_id
    }
}

# --------------------------------------------------
# AI Function
# --------------------------------------------------

async def ask_ai(prompt):

    response = await coordinator.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        },
        config=config
    )

    return response["messages"][-1].content

# --------------------------------------------------
# Chat Bubble Renderer
# --------------------------------------------------

import markdown as _md_lib

_MD_EXTENSIONS = ["extra", "sane_lists", "nl2br"]

def render_bubble(role: str, content: str):
    """Render a single chat message as a custom styled bubble.

    Assistant answers are typically markdown (headings, bold, bullet
    lists) — we convert that markdown to HTML so it renders with
    proper structure instead of appearing as one flat block of text.
    """
    avatar = "🧑" if role == "user" else "💍"
    content_html = _md_lib.markdown(content, extensions=_MD_EXTENSIONS)

    st.markdown(
        f"""
        <div class="chat-row {role}">
            <div class="chat-avatar {role}">{avatar}</div>
            <div class="chat-bubble {role}">{content_html}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# Display Chat History
# --------------------------------------------------

for message in st.session_state.messages:
    render_bubble(message["role"], message["content"])

# --------------------------------------------------
# Chat Input
# --------------------------------------------------

prompt = st.chat_input("Ask me anything about your wedding...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    render_bubble("user", prompt)

    with st.spinner("✨ AI Agents are planning your wedding..."):

        answer = asyncio.run(
            ask_ai(prompt)
        )

        # Normalize Response
        answer = normalize_response(answer)

    render_bubble("assistant", answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown(
    """
    <div class="app-footer">
        Powered by <b>LangChain Multi-Agent Architecture</b><br>
        Built with ❤️ by <b>Wakeel Ahmad</b>
    </div>
    """,
    unsafe_allow_html=True
)
