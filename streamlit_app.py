import streamlit as st
import asyncio
import uuid
import time

from agents.coordinator import coordinator
from utils.response_normalizer import normalize_response

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="AI Wedding Planner",
    page_icon="W",
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

@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Main app background - warm ivory, premium feel */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg, #FBFAF7 0%, #F6F4EE 100%);
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
    background: linear-gradient(180deg, #0F2043 0%, #0A1630 100%);
    color: #E9E4D8;
}

[data-testid="stSidebar"] * {
    color: #E9E4D8 !important;
}

[data-testid="stSidebar"] h1 {
    font-family: 'Playfair Display', serif;
    font-weight: 700;
    font-size: 1.55rem;
    padding-bottom: 0.2rem;
}

.sidebar-divider {
    border: none;
    border-top: 1px solid rgba(201, 162, 76, 0.2);
    margin: 1rem 0;
}

.sidebar-section-title {
    font-size: 0.72rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #C9A24C !important;
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
    background: rgba(201, 162, 76, 0.1);
    border: 1px solid rgba(201, 162, 76, 0.35);
    color: #C9A24C !important;
    padding: 3px 10px;
    border-radius: 20px;
    font-size: 0.72rem;
    margin: 3px 4px 3px 0;
}

/* Sidebar buttons (New Chat) */
[data-testid="stSidebar"] button {
    background: linear-gradient(135deg, #D9B25F, #B8892E) !important;
    color: #14213D !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}

[data-testid="stSidebar"] button:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 16px rgba(201, 162, 76, 0.35);
}

/* History list buttons: quieter style than the New Chat button,
   left-aligned with truncated text, highlighted when active */
[data-testid="stSidebar"] button[kind="secondary"] {
    background: rgba(233, 228, 216, 0.05) !important;
    border: 1px solid rgba(233, 228, 216, 0.12) !important;
    color: #C7CADA !important;
    font-weight: 400 !important;
    text-align: left !important;
    justify-content: flex-start !important;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    display: block !important;
}

[data-testid="stSidebar"] button[kind="secondary"]:hover {
    background: rgba(233, 228, 216, 0.1) !important;
    box-shadow: none;
    transform: none;
}

[data-testid="stSidebar"] button[kind="primary"] {
    text-align: left !important;
    justify-content: flex-start !important;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    display: block !important;
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
    box-shadow: 0 10px 30px rgba(15, 32, 67, 0.18);
    background-image:
        linear-gradient(180deg, rgba(10,22,48,0.6) 0%, rgba(10,22,48,0.8) 100%),
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
    font-family: 'Playfair Display', serif;
    color: #FFFFFF;
    font-size: 2.5rem;
    font-weight: 700;
    margin: 0;
    text-shadow: 0 2px 12px rgba(0,0,0,0.35);
}

.hero-divider {
    width: 60px;
    height: 2px;
    background: #C9A24C;
    margin: 0.8rem auto;
}

.hero-subtitle {
    color: #E9D9AE;
    font-size: 1.02rem;
    font-weight: 400;
    letter-spacing: 0.4px;
    text-shadow: 0 2px 8px rgba(0,0,0,0.35);
}

/* --------------------------------------------------
   Feature / Quick-Prompt Buttons
-------------------------------------------------- */
.st-key-feature_buttons {
    margin-bottom: 1.6rem;
}

.st-key-feature_buttons button {
    background: #FFFFFF !important;
    color: #14213D !important;
    border: 1px solid #E9E4D8 !important;
    border-radius: 14px !important;
    padding: 1rem 0.5rem !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    box-shadow: 0 4px 14px rgba(15, 32, 67, 0.06) !important;
    transition: transform 0.15s ease, box-shadow 0.15s ease, border-color 0.15s ease;
}

.st-key-feature_buttons button:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 24px rgba(201, 162, 76, 0.22) !important;
    border-color: #C9A24C !important;
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
    font-size: 0.85rem;
    font-weight: 700;
    color: #FFFFFF;
}

.chat-avatar.user {
    background: linear-gradient(135deg, #1B3A6B, #0F2043);
}

.chat-avatar.assistant {
    background: linear-gradient(135deg, #D9B25F, #B8892E);
    color: #14213D;
}

.chat-bubble {
    max-width: 72%;
    padding: 0.75rem 1.05rem;
    font-size: 0.96rem;
    line-height: 1.55;
}

.chat-bubble.user {
    background: linear-gradient(135deg, #1B3A6B, #0F2043);
    color: #FFFFFF;
    border-radius: 18px 18px 4px 18px;
    box-shadow: 0 4px 14px rgba(15, 32, 67, 0.25);
}

.chat-bubble.user p, .chat-bubble.user * {
    color: #FFFFFF !important;
}

.chat-bubble.assistant {
    background: #FFFFFF;
    color: #1C2B45;
    border-radius: 18px 18px 18px 4px;
    box-shadow: 0 4px 14px rgba(15, 32, 67, 0.07);
    border: 1px solid #ECE7DA;
}

.chat-bubble p {
    margin: 0 0 0.5rem 0;
}

.chat-bubble p:last-child {
    margin-bottom: 0;
}

.chat-bubble h1, .chat-bubble h2, .chat-bubble h3, .chat-bubble h4 {
    font-family: 'Playfair Display', serif;
    margin: 0.6rem 0 0.4rem 0;
    font-weight: 700;
    line-height: 1.3;
}

.chat-bubble h1 { font-size: 1.25rem; }
.chat-bubble h2 { font-size: 1.15rem; }
.chat-bubble h3 { font-size: 1.05rem; color: #B8892E; }
.chat-bubble h4 { font-size: 0.98rem; color: #B8892E; }

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
    color: #0F2043;
}

.chat-bubble.user strong {
    color: #FFFFFF !important;
}

.chat-bubble em {
    color: inherit;
}

.chat-bubble code {
    background: rgba(201, 162, 76, 0.12);
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
    border: 1px solid #ECE7DA;
    padding: 6px 10px;
    text-align: left;
}

.chat-bubble th {
    background: #FAF6EC;
}

.chat-bubble hr {
    border: none;
    border-top: 1px solid #ECE7DA;
    margin: 0.6rem 0;
}

/* --------------------------------------------------
   Chat input box (bottom fixed area)
-------------------------------------------------- */
[data-testid="stBottomBlockContainer"],
[data-testid="stBottom"] > div {
    background: linear-gradient(180deg, rgba(246,244,238,0) 0%, #F6F4EE 40%) !important;
}

[data-testid="stChatInput"] {
    background: transparent !important;
}

[data-testid="stChatInput"] > div {
    background: #FFFFFF !important;
    border: 1px solid #E9E4D8 !important;
    border-radius: 26px !important;
    box-shadow: 0 6px 20px rgba(15, 32, 67, 0.08) !important;
    padding: 2px 6px !important;
}

[data-testid="stChatInput"] > div:focus-within {
    border: 1px solid #C9A24C !important;
    box-shadow: 0 6px 20px rgba(201, 162, 76, 0.22) !important;
}

[data-testid="stChatInput"] textarea {
    border: none !important;
    box-shadow: none !important;
    font-family: 'Inter', sans-serif !important;
    color: #1C2B45 !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #A9A69A !important;
}

/* Send button */
[data-testid="stChatInput"] button {
    background: linear-gradient(135deg, #D9B25F, #B8892E) !important;
    border-radius: 50% !important;
    border: none !important;
}

[data-testid="stChatInput"] button svg {
    fill: #14213D !important;
}

</style>
"""

st.markdown(_CSS.replace("__HERO_IMAGE_URL__", HERO_IMAGE_URL), unsafe_allow_html=True)

# --------------------------------------------------
# Session State
# --------------------------------------------------
# We keep a dictionary of chat sessions so the sidebar can show
# previous conversations, not just the current one.
#
# st.session_state.sessions = {
#     thread_id: {"title": "First user message...", "messages": [...]},
#     ...
# }

if "sessions" not in st.session_state:
    st.session_state.sessions = {}

if "active_thread_id" not in st.session_state:
    new_id = str(uuid.uuid4())
    st.session_state.sessions[new_id] = {"title": "New Chat", "messages": []}
    st.session_state.active_thread_id = new_id

active_id = st.session_state.active_thread_id
active_session = st.session_state.sessions[active_id]

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.title("AI Wedding Planner")

    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)

    if st.button("New Chat", use_container_width=True, type="primary"):
        new_id = str(uuid.uuid4())
        st.session_state.sessions[new_id] = {"title": "New Chat", "messages": []}
        st.session_state.active_thread_id = new_id
        st.rerun()

    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-section-title">History</div>', unsafe_allow_html=True)

    # Most recent sessions first
    for tid in reversed(list(st.session_state.sessions.keys())):
        session = st.session_state.sessions[tid]
        label = session["title"]
        is_active = (tid == active_id)

        button_type = "primary" if is_active else "secondary"

        if st.button(label, key=f"history_{tid}", use_container_width=True, type=button_type):
            st.session_state.active_thread_id = tid
            st.rerun()

    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-section-title">About Project</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="sidebar-credit">
        An AI-powered wedding planning assistant that helps you plan venue,
        budget, catering, decoration and timeline, all through a
        conversational multi-agent system.
        </div>
        """,
        unsafe_allow_html=True
    )

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
            <div class="hero-title">AI Wedding Planner</div>
            <div class="hero-divider"></div>
            <div class="hero-subtitle">Plan Your Dream Wedding — Powered by LangChain AI Agents</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Feature / Quick-Prompt Buttons
# --------------------------------------------------
# Clicking one of these sends a ready-made question to the AI,
# instead of the user having to type it out.

FEATURE_PROMPTS = {
    "Venue": "Suggest some venue options for my wedding, with pricing and capacity.",
    "Budget": "Help me plan and allocate my wedding budget.",
    "Catering": "Suggest catering options and menu ideas for my wedding.",
    "Decoration": "Suggest wedding decoration themes and ideas.",
    "Timeline": "Create a wedding day schedule and timeline.",
}

card_prompt = None

with st.container(key="feature_buttons"):
    cols = st.columns(len(FEATURE_PROMPTS))
    for col, (label, canned_prompt) in zip(cols, FEATURE_PROMPTS.items()):
        with col:
            if st.button(label, key=f"card_{label}", use_container_width=True):
                card_prompt = canned_prompt

# --------------------------------------------------
# LangGraph Config
# --------------------------------------------------

config = {
    "configurable": {
        "thread_id": active_id
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
    avatar = "U" if role == "user" else "W"
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


def render_bubble_streaming(content: str, delay: float = 0.02):
    """Render the assistant's answer word-by-word, like ChatGPT typing.

    Uses a single placeholder that gets re-rendered with progressively
    more of the text on each step, instead of dumping the full answer
    at once.
    """
    placeholder = st.empty()
    words = content.split(" ")
    shown = ""

    for word in words:
        shown += word + " "
        content_html = _md_lib.markdown(shown, extensions=_MD_EXTENSIONS)

        placeholder.markdown(
            f"""
            <div class="chat-row assistant">
                <div class="chat-avatar assistant">W</div>
                <div class="chat-bubble assistant">{content_html}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        time.sleep(delay)

# --------------------------------------------------
# Display Chat History
# --------------------------------------------------

for message in active_session["messages"]:
    render_bubble(message["role"], message["content"])

# --------------------------------------------------
# Chat Input
# --------------------------------------------------

typed_prompt = st.chat_input("Ask me anything about your wedding...")
prompt = card_prompt or typed_prompt

if prompt:

    active_session["messages"].append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Title the session after the first message, like ChatGPT does
    if active_session["title"] == "New Chat":
        active_session["title"] = (prompt[:30] + "...") if len(prompt) > 30 else prompt

    render_bubble("user", prompt)

    with st.spinner("AI agents are planning your wedding..."):

        answer = asyncio.run(
            ask_ai(prompt)
        )

        # Normalize Response
        answer = normalize_response(answer)

    render_bubble_streaming(answer)

    active_session["messages"].append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.rerun()
