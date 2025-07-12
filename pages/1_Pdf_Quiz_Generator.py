import streamlit as st
from dotenv import load_dotenv
from pypdf import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain_groq import ChatGroq
from htmlTemplates import css, bot_template, user_template
import os

# Custom CSS for enhanced styling
def load_custom_css():
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
        .chat-input {
            background: #f8f9fa;
            border: 2px solid #e9ecef;
            border-radius: 25px;
            padding: 0.8rem 1.5rem;
            margin: 1rem 0;
        }
        .sidebar-section {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }
        .process-btn {
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 0.8rem 2rem;
            border-radius: 25px;
            font-weight: 600;
            width: 100%;
            margin-top: 1rem;
            cursor: pointer;
        }
        .stFileUploader > div {
            border: 2px dashed #667eea;
            border-radius: 10px;
            padding: 2rem;
            text-align: center;
        }
        /* Hide default Streamlit styling */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# STEP 1: Extract PDF Text
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# STEP 2: Split Text into Chunks
def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

# STEP 3: Create Vectorstore using HuggingFace Embeddings
def get_vectorstore(text_chunks):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

# STEP 4: Create Chat Chain
groq_api_key = os.environ.get("GROQ_API_KEY")
def get_conversation_chain(vectorstore):
    llm = ChatGroq(
        temperature=0,
        model_name="llama-3.3-70b-versatile",
        groq_api_key=groq_api_key
    )
    memory = ConversationBufferMemory(
        memory_key='chat_history', 
        return_messages=True
    )
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

# STEP 5: Handle User Input
def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)

# MAIN APP
def main():
    load_dotenv()
    st.set_page_config(
        page_title="PDF Chat Assistant",
        page_icon="📚",
        layout="wide"
    )
    
    # Load custom CSS
    load_custom_css()
    st.write(css, unsafe_allow_html=True)

    # Initialize session state
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    # Main header
    st.markdown("""
    <div class="main-header">
        <h1>📚 PDF Chat Assistant</h1>
        <p>Ask questions about your PDF documents using AI</p>
    </div>
    """, unsafe_allow_html=True)

    # Chat input
    user_question = st.text_input(
        "💬 Ask a question about your documents:",
        placeholder="What is the main topic of this document?",
        key="chat_input"
    )
    
    if user_question:
        if st.session_state.conversation is None:
            st.warning("⚠️ Please upload and process PDF documents first!")
        else:
            handle_userinput(user_question)

    # Sidebar
    with st.sidebar:
        
        st.markdown("### 📁 Upload Documents")
        
        pdf_docs = st.file_uploader(
            "Choose PDF files",
            accept_multiple_files=True,
            type="pdf",
            help="Upload one or more PDF documents"
        )
        
        if pdf_docs:
            st.success(f"✅ {len(pdf_docs)} file(s) uploaded")
            for pdf in pdf_docs:
                st.write(f"📄 {pdf.name}")
        
        if st.button("🚀 Process Documents", key="process"):
            if pdf_docs:
                with st.spinner("Processing your documents..."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    vectorstore = get_vectorstore(text_chunks)
                    st.session_state.conversation = get_conversation_chain(vectorstore)
                st.success("✅ Documents processed successfully!")
            else:
                st.error("❌ Please upload PDF files first!")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Instructions
        st.markdown("### 📝 How to Use")
        st.markdown("""
        1. **Upload** your PDF files above
        2. **Process** the documents 
        3. **Ask** questions in the chat
        4. **Get** intelligent responses
        """)

if __name__ == '__main__':
    main()