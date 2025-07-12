# Study-Suite

A Streamlit app for AI-powered learning: chat with PDFs, generate quizzes and MCQs with explanations. Built using LangChain, Groq API, Hugging Face, and Streamlit for modern study support.

## Features
- **PDF Chat & Quiz Generator:** Chat with your uploaded PDF documents and generate contextual quizzes.
- **MCQ Generator with Explanations:** Automatically create multiple-choice questions with detailed explanations from your study material.
- **Modern UI:** Clean, responsive interface with custom CSS.
- **Powered by:** LangChain, Groq API, Hugging Face, and Streamlit.

## Technology Stack
- Python 3.12+
- Streamlit
- LangChain
- Groq API
- Hugging Face

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/vishnuprakash-777/Study-Suite.git
   cd Study-Suite
   ```

2. **Create and activate a virtual environment (recommended):**
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the project root.
   - Add your API keys and configuration as needed (e.g., Groq API, Hugging Face credentials).

5. **Run the app:**
   ```sh
   streamlit run Home.py
   ```

## Usage
- Select a feature from the sidebar after launching the app.
- Upload your PDF to chat with it or generate quizzes.
- Use the MCQ generator for instant questions and explanations from your study material.
