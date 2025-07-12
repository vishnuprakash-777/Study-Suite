import streamlit as st

# Page config
st.set_page_config(
    page_title="Study Suite - Your Learning Companion", 
    page_icon="📚", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    .main-header h1 {
        font-size: 3.5rem;
        margin-bottom: 0.5rem;
        font-weight: 700;
    }
    
    .main-header p {
        font-size: 1.2rem;
        opacity: 0.9;
        margin-bottom: 0;
    }
    
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid #e0e6ed;
        margin-bottom: 1.5rem;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.15);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    .feature-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 1rem;
    }
    
    .feature-description {
        color: #555;
        line-height: 1.6;
        font-size: 1rem;
    }
    
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 3rem 0;
        padding: 2rem;
        background: #f8f9fa;
        border-radius: 15px;
    }
    
    .stat-item {
        text-align: center;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: #667eea;
        display: block;
    }
    
    .stat-label {
        color: #666;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .cta-section {
        text-align: center;
        padding: 3rem 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        margin: 3rem 0;
    }
    
    .cta-section h2 {
        margin-bottom: 1rem;
        font-size: 2.2rem;
    }
    
    .cta-section p {
        font-size: 1.1rem;
        opacity: 0.9;
        margin-bottom: 2rem;
    }
    
    .footer {
        text-align: center;
        padding: 2rem 0;
        color: #666;
        border-top: 1px solid #e0e6ed;
        margin-top: 3rem;
    }
    
    .tech-stack {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin: 2rem 0;
    }
    
    .tech-item {
        background: #f8f9fa;
        padding: 0.8rem 1.5rem;
        border-radius: 25px;
        font-size: 0.9rem;
        color: #555;
        border: 1px solid #e0e6ed;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown("""
<div class="main-header">
    <h1>📚 Study Suite</h1>
    <p>Your Comprehensive Learning Companion</p>
</div>
""", unsafe_allow_html=True)

# Introduction section
st.markdown("""
<div style="text-align: center; margin: 2rem 0;">
    <p style="font-size: 1.2rem; color: #555; line-height: 1.6;">
        Revolutionize your learning experience with AI-powered tools designed for students, educators, and lifelong learners. 
        Transform any document into an interactive learning session with intelligent conversations and adaptive quizzes.
    </p>
</div>
""", unsafe_allow_html=True)

# Features section
st.markdown("## 🚀 Powerful Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">🔍</span>
        <div class="feature-title">PDF Chat & Quiz Generator</div>
        <div class="feature-description">
            Engage in intelligent conversations with your uploaded PDF documents. Ask questions, get instant answers, 
            and generate contextual quiz questions to test your understanding. Perfect for research papers, textbooks, 
            and study materials.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">📝</span>
        <div class="feature-title">MCQ Generator with Explanations</div>
        <div class="feature-description">
            Automatically generate multiple-choice questions from your study material with varying difficulty levels. 
            Get instant feedback with correct answers and detailed explanations to reinforce your learning.
        </div>
    </div>
    """, unsafe_allow_html=True)

# Stats section
st.markdown("""
<div class="stats-container">
    <div class="stat-item">
        <span class="stat-number">∞</span>
        <span class="stat-label">Documents Supported</span>
    </div>
    <div class="stat-item">
        <span class="stat-number">AI</span>
        <span class="stat-label">Powered Intelligence</span>
    </div>
    <div class="stat-item">
        <span class="stat-number">24/7</span>
        <span class="stat-label">Learning Support</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Technology stack
st.markdown("## 🛠️ Built with Cutting-Edge Technology")
st.markdown("""
<div class="tech-stack">
    <div class="tech-item">🤖 LangChain</div>
    <div class="tech-item">⚡ Groq API</div>
    <div class="tech-item">🤗 Hugging Face</div>
    <div class="tech-item">🎯 Streamlit</div>
</div>
""", unsafe_allow_html=True)

# Call to action
st.markdown("""
<div class="cta-section">
    <h2>Ready to Transform Your Learning?</h2>
    <p>Join thousands of learners who have already enhanced their study experience with Study Suite.</p>
    <p style="font-size: 1.1rem; font-weight: 600;">👈 Get started by selecting a feature from the sidebar</p>
</div>
""", unsafe_allow_html=True)



# Footer
