import streamlit as st
from dotenv import load_dotenv
from pypdf import PdfReader
from langchain_groq import ChatGroq
import os

# Custom CSS for enhanced styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .question-card {
        background: #fff;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }
    .correct-answer {
        color: #22bb33;
        font-weight: bold;
    }
    .explanation {
        color: #555;
        font-style: italic;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="MCQ Generator & Answers", page_icon="📝", layout="wide")

# Styled header
st.markdown("""
<div class="main-header">
    <h1>📝 MCQ Generator & Answers</h1>
    <p>Generate multiple-choice questions from your PDFs and see correct answers with explanations instantly!</p>
</div>
""", unsafe_allow_html=True)

# Extract text from PDFs
def extract_text_from_pdfs(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        reader = PdfReader(pdf)
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
    return text

# Prompt template to instruct LLM
def generate_mcq_prompt(text):
    return f"""
From the following text, generate up to 5 MCQs. Each should include:
- A question
- 4 options labeled A, B, C, D
- The correct answer (A/B/C/D)
- A short explanation

Use this exact format:

Q: Question here  
A. Option A  
B. Option B  
C. Option C  
D. Option D  
Correct Answer: A  
Explanation: Explanation here

Text:
{text}
"""

# Call Groq LLM with prompt
def call_groq(prompt):
    llm = ChatGroq(
        temperature=0.2,
        model_name="llama-3.3-70b-versatile",  # Updated model name
        groq_api_key=groq_api_key
    )
    response = llm.invoke(prompt)
    return response.content if hasattr(response, 'content') else str(response)

# Parse MCQs from the LLM response
def parse_mcqs(raw_text):
    questions = []
    parts = raw_text.split("Q:")
    for part in parts[1:]:
        lines = part.strip().split("\n")
        question = lines[0]
        options = lines[1:5]
        correct_line = [line for line in lines if line.startswith("Correct Answer")]
        explanation_line = [line for line in lines if line.startswith("Explanation")]

        correct = correct_line[0].split(":")[1].strip() if correct_line else ""
        explanation = explanation_line[0].split(":", 1)[1].strip() if explanation_line else ""

        questions.append({
            "question": question,
            "options": options,
            "correct": correct,
            "explanation": explanation
        })
    return questions

# Sidebar uploader
with st.sidebar:
    st.header("📚 Upload your PDFs")
    pdf_docs = st.file_uploader("Upload PDFs", accept_multiple_files=True)

# Main logic
if pdf_docs:
    if st.button("Generate Quiz"):
        with st.spinner("Extracting text and generating questions..."):
            raw_text = extract_text_from_pdfs(pdf_docs)
            prompt = generate_mcq_prompt(raw_text)
            response = call_groq(prompt)
            questions = parse_mcqs(response)

            if questions:
                st.success("✅ Quiz Generated Successfully!")
                st.subheader("📝 Here are the questions with correct answers and explanations:")
                for i, q in enumerate(questions):
                    with st.container():
                        
                        st.markdown(f"<b>Q{i+1}:</b> {q['question']}", unsafe_allow_html=True)
                        for opt in q['options']:
                            if opt.startswith(q['correct'] + '.'):
                                st.markdown(f'<span class="correct-answer">✅ {opt} (Correct Answer)</span>', unsafe_allow_html=True)
                            else:
                                st.markdown(f'• {opt}', unsafe_allow_html=True)
                        st.markdown(f'<div class="explanation">💡 <b>Explanation:</b> {q["explanation"]}</div>', unsafe_allow_html=True)
                        st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning("⚠️ No questions could be generated. Try another document.")
