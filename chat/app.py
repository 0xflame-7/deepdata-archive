import streamlit as st
import fitz  # PyMuPDF
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ Gemini API key not found. Please set GEMINI_API_KEY in your .env file.")
    st.stop()

# Fix: Configure with proper API key
genai.configure(api_key=api_key)

# Fix: Use full model name
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-001")

st.set_page_config(page_title="Chat with PDFs", layout="centered")
st.title("📄 Chat with PDFs using Gemini")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting PDF..."):
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        pdf_text = "\n".join(page.get_text() for page in doc)

    st.success("PDF Loaded ✅")
    st.text_area("Preview", pdf_text[:1000] + "..." if len(pdf_text) > 1000 else pdf_text, height=200)

    question = st.text_input("Ask your question")

    if question:
        with st.spinner("Gemini is thinking..."):
            prompt = f"""
Use the PDF content below to answer the question.

PDF Content:
\"\"\"
{pdf_text[:12000]}
\"\"\"

Question: {question}
"""
            try:
                response = model.generate_content(prompt)
                st.subheader("💡 Answer:")
                st.write(response.text)
            except Exception as e:
                st.error(f"❌ Gemini Error: {e}")
