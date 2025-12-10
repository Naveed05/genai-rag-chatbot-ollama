import streamlit as st
from rag_utils import build_vectorstore, build_rag_chain

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="Advanced Local RAG Chatbot",
    layout="wide",
    page_icon="🤖"
)

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.header("⚙️ Settings")

    model_name = st.selectbox(
        "LLM Model (Ollama)",
        ["mistral", "llama3", "qwen2", "gemma"],
        index=0
    )

    temperature = st.slider(
        "Creativity (Temperature)",
        0.0, 1.5, 0.2, 0.1
    )

    chunk_size = st.slider(
        "Chunk Size",
        200, 1500, 600, 50
    )

    chunk_overlap = st.slider(
        "Chunk Overlap",
        0, 300, 80, 10
    )

    st.divider()

    if st.button("🧹 Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

    st.divider()

    st.caption("Built with ❤️ using: TensorFlow • FAISS • Ollama • Streamlit")

# -----------------------------
# MAIN PAGE TITLE
# -----------------------------
st.title("🤖 Advanced Local RAG Chatbot")
st.write("Upload a PDF and chat with it. Everything runs **offline**, powered by **FAISS + TensorFlow + Ollama**.")

# -----------------------------
# UPLOAD AREA
# -----------------------------
uploaded_pdf = st.file_uploader("📄 Upload PDF", type=["pdf"])

# SESSION STATE INIT
if "vstore" not in st.session_state:
    st.session_state.vstore = None

if "rag" not in st.session_state:
    st.session_state.rag = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -----------------------------
# PROCESS PDF
# -----------------------------
if uploaded_pdf:
    st.success(f"📘 Loaded File: **{uploaded_pdf.name}**")

    with st.spinner("🔍 Building vector store (GPU/CPU embeddings)..."):
        st.session_state.vstore = build_vectorstore(uploaded_pdf)
        st.session_state.rag = build_rag_chain(st.session_state.vstore)

    st.toast("PDF processed! Start chatting.", icon="🤖")

# -----------------------------
# CHAT INPUT
# -----------------------------
user_message = st.chat_input("Type your question about the PDF...")

if user_message:
    # Save user message
    st.session_state.chat_history.append(("user", user_message))

    with st.chat_message("user"):
        st.write(user_message)

    # Generate answer
    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤖"):
            answer = st.session_state.rag(user_message)

            # Streaming answer simulation
            placeholder = st.empty()
            displayed = ""

            for char in answer:
                displayed += char
                placeholder.markdown(displayed)
            st.session_state.chat_history.append(("assistant", answer))

# -----------------------------
# DISPLAY CHAT HISTORY
# -----------------------------
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(message)
