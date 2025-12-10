📘 Local PDF RAG Chatbot (TensorFlow + FAISS + Ollama + Streamlit)
⚡ Fully Offline • GPU Accelerated • Mistral / Gemma2 / Qwen2 Support

This project is a fully offline Retrieval-Augmented Generation (RAG) chatbot that lets you upload any PDF and ask questions about its content. The system uses:
TensorFlow Embeddings (Universal Sentence Encoder or USE-Large)
FAISS Vector Search for fast similarity retrieval
Ollama LLMs (Mistral, Gemma2, Qwen2, etc.)
Streamlit for a modern ChatGPT-like UI
Everything runs completely locally — your data never leaves your machine.

🚀 Features
🔍 1. Offline PDF Question Answering
Upload any PDF (notes, research paper, textbook, legal doc, manual) and ask queries about its content.

⚡ 2. GPU-Optimized TensorFlow Embeddings
High-speed embedding generation
Supports CUDA-enabled GPUs
Compatible with USE, USE-Large, or any TF Hub model

🧠 3. FAISS Vector Search
Fast retrieval even on large PDFs
Efficient similarity search
Scalable to thousands of chunks

🤖 4. Local LLMs via Ollama
Choose from locally installed models:
Mistral 7B (balanced)
Gemma2 (Google’s stronger reasoning)
Qwen2 (high accuracy)
Llama 3.1 (optional)

No API keys. No internet required.

💬 5. Advanced Chat UI
ChatGPT-style message bubbles
Sidebar settings
Model selector
Streaming responses
Clear/Reset chat
Chunk size controls
Temperature slider

🏗️ Project Structure
genai-rag-chatbot-ollama/
│
├── src/
│   ├── app.py              # Streamlit UI
│   ├── rag_utils.py        # RAG logic (embeddings + FAISS + LLM)
│   ├── pdf_loader.py       # PDF text extraction
│
├── requirements.txt
└── README.md

⚙️ Installation
1️⃣ Clone the Repo
git clone https://github.com/Naveed05/genai-rag-chatbot-ollama.git
cd genai-rag-chatbot-ollama

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Install Ollama
Download from:
https://ollama.com/download

4️⃣ Pull a Model
ollama pull mistral
# or
ollama pull gemma2
# or
ollama pull qwen2

5️⃣ Run the App
streamlit run src/app.py

🧩 How It Works
1. PDF Text Extraction
pdf_loader.py uses PyMuPDF (fitz) to extract clean text.

2. Text Chunking & Embeddings
rag_utils.py:
Chunks text
Creates embeddings using TensorFlow (USE)
Stores them in a FAISS index

3. RAG Retrieval
Queries are embedded → top chunks retrieved → passed to LLM.

4. LLM Answer Generation
Ollama processes the prompt and returns a context-aware response.

🧠 Use Cases
Study helper for textbooks/notes
Legal document question answering
Research paper summarization
Corporate internal documents
Product/manual-based Q&A
Offline classroom assistant

🌟 Why This Project Is Special
✔ 100% offline & private
✔ No API keys
✔ Works on CPU or GPU
✔ Professional, modular code
✔ Supports multiple LLMs
✔ Flexible architecture (easy to extend)

🛠️ Upcoming Add-ons
Multi-PDF RAG
Embedding caching
Vision + PDF image OCR
Conversation memory
Dark mode UI

🤝 Contributing

Pull requests are welcome! Feel free to fork and enhance the system.
