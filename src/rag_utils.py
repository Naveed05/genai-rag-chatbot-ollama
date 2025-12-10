import numpy as np
import tensorflow_hub as hub
import faiss
from pdf_loader import extract_text_from_pdf
import ollama

# Load TensorFlow Embedding Model (USE v4)
embedder = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

def build_vectorstore(pdf_file):
    """Extract text → chunk → embed → store into FAISS index."""

    # Extract PDF text
    text = extract_text_from_pdf(pdf_file)

    # Simple chunking by paragraphs
    chunks = [c.strip() for c in text.split("\n\n") if c.strip()]

    # Generate embeddings
    embeddings = embedder(chunks).numpy().astype("float32")

    # Create FAISS index
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    return {
        "index": index,
        "texts": chunks,
        "embed": embedder
    }


def build_rag_chain(vstore):

    def ask(question):

        # Encode question
        q_embed = vstore["embed"]([question]).numpy().astype("float32")

        # Search FAISS
        _, I = vstore["index"].search(q_embed, k=3)

        # Retrieve relevant chunks
        context = "\n\n".join(vstore["texts"][i] for i in I[0])

        # Prepare prompt for LLM
        prompt = f"""
You are an expert assistant. Answer ONLY using the context.

Context:
{context}

Question: {question}

Answer:
"""

        # Query Ollama (Mistral)
        response = ollama.chat(
            model="mistral",
            messages=[{"role": "user", "content": prompt}]
        )

        return response["message"]["content"]

    return ask
