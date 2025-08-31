import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="EduMate - Your AI Study Buddy",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dark theme and beautiful UI
st.markdown("""
<style>
    /* Main container styling */
    .main-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 2rem 1rem;
    }
    
    /* Header styling */
    .header {
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Chat container */
    .chat-container {
        background: #1e1e1e;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid #333;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }
    
    /* User message bubble */
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 20px 20px 5px 20px;
        margin: 0.5rem 0 0.5rem auto;
        max-width: 80%;
        word-wrap: break-word;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
    }
    
    /* Bot message bubble */
    .bot-message {
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
        color: #ecf0f1;
        padding: 1rem 1.5rem;
        border-radius: 20px 20px 20px 5px;
        margin: 0.5rem auto 0.5rem 0;
        max-width: 80%;
        word-wrap: break-word;
        box-shadow: 0 4px 12px rgba(44, 62, 80, 0.3);
        border-left: 4px solid #3498db;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.6rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    
    /* Input box styling */
    .stTextInput > div > div > input {
        background-color: #2c3e50;
        color: white;
        border: 2px solid #34495e;
        border-radius: 15px;
        padding: 0.8rem 1rem;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #3498db;
        box-shadow: 0 0 20px rgba(52, 152, 219, 0.3);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #1a1a1a;
    }
    
    /* Error/Success messages */
    .stAlert {
        border-radius: 10px;
        border: none;
    }
    
    /* Loading spinner color */
    .stSpinner > div {
        border-top-color: #3498db !important;
    }
    
    /* Custom spacing */
    .space {
        margin: 1rem 0;
    }
    
    /* Bot name styling */
    .bot-name {
        color: #3498db;
        font-weight: 600;
        margin-bottom: 0.5rem;
        display: block;
    }
    
    /* User name styling */
    .user-name {
        color: #ecf0f1;
        font-weight: 600;
        margin-bottom: 0.5rem;
        display: block;
        text-align: right;
    }
</style>
""", unsafe_allow_html=True)

def get_api_response(messages, api_key):
    """
    Send request to OpenRouter API and return the response
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "http://localhost:8501",  # Streamlit default
        "X-Title": "EduMate Study Assistant",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "openai/gpt-4o-mini",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 1500,
        "stream": False
    }
    
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=30
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"API request failed: {str(e)}")

def display_chat_message(message, is_user=True):
    """
    Display a chat message with proper styling
    """
    if is_user:
        st.markdown(f"""
        <div class="user-name">You</div>
        <div class="user-message">{message}</div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="bot-name">🤖 EduMate</div>
        <div class="bot-message">{message}</div>
        """, unsafe_allow_html=True)

def main():
    """
    Main application function
    """
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    # App header
    st.markdown('<div class="header">📚 EduMate – Your AI Study Buddy</div>', unsafe_allow_html=True)
    
    # Subtitle
    st.markdown("""
    <div style="text-align: center; color: #7f8c8d; font-size: 1.2rem; margin-bottom: 2rem;">
        Ask me anything about computer science, programming, or study topics!
    </div>
    """, unsafe_allow_html=True)
    
    # Check for API key
    api_key = os.getenv("OPENROUTER_API_KEY", "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")
    
    if not api_key:
        st.error("⚠️ OpenRouter API key not found! Please add OPENROUTER_API_KEY to your .env file.")
        st.info("💡 Create a .env file in your project root and add: OPENROUTER_API_KEY=your_api_key_here")
        return
    
    # Create two columns for input and buttons
    col1, col2, col3 = st.columns([6, 1.5, 1.5])
    
    with col1:
        user_input = st.text_input(
            "Your question:",
            placeholder="e.g., Explain binary search in simple terms...",
            key="user_input",
            label_visibility="collapsed"
        )
    
    with col2:
        ask_button = st.button("🚀 Ask", type="primary", use_container_width=True)
    
    with col3:
        clear_button = st.button("🗑️ Clear", use_container_width=True)
    
    # Handle clear chat
    if clear_button:
        st.session_state.messages = []
        st.session_state.chat_history = []
        st.success("✨ Chat history cleared!")
        st.rerun()
    
    # Handle ask button
    if ask_button and user_input.strip():
        # Add user message to history
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Prepare messages for API (include system message)
        api_messages = [
            {
                "role": "system", 
                "content": "You are EduMate, a helpful and friendly study assistant for university students. You specialize in explaining computer science concepts, programming, mathematics, and other academic topics in simple, clear terms. Always be encouraging, patient, and provide examples when helpful. Keep your responses concise but comprehensive."
            }
        ]
        api_messages.extend(st.session_state.chat_history)
        
        # Show loading spinner
        with st.spinner("🤔 EduMate is thinking..."):
            try:
                # Get response from API
                response = get_api_response(api_messages, api_key)
                bot_response = response["choices"][0]["message"]["content"]
                
                # Add bot response to history
                st.session_state.chat_history.append({"role": "assistant", "content": bot_response})
                
                # Clear input box
                st.session_state.user_input = ""
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.info("💡 Please check your internet connection and API key.")
    
    # Display chat history
    if st.session_state.chat_history:
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                display_chat_message(message["content"], is_user=True)
                st.markdown('<div class="space"></div>', unsafe_allow_html=True)
            elif message["role"] == "assistant":
                display_chat_message(message["content"], is_user=False)
                st.markdown('<div class="space"></div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Show helpful tips in sidebar
    with st.sidebar:
        st.markdown("## 💡 Tips for Better Answers")
        st.markdown("""
        - Be specific in your questions
        - Ask for examples when needed
        - Request step-by-step explanations
        - Ask follow-up questions for clarity
        """)
        
        st.markdown("## 📚 Example Questions")
        st.markdown("""
        - "Explain recursion with an example"
        - "What's the difference between arrays and linked lists?"
        - "How does binary search work?"
        - "What is Big O notation?"
        - "Explain object-oriented programming concepts"
        """)
        
        st.markdown("## 🔧 Features")
        st.markdown("""
        - ✅ Persistent chat history
        - ✅ Context-aware responses  
        - ✅ Computer science focused
        - ✅ Student-friendly explanations
        - ✅ Dark theme interface
        """)

if __name__ == "__main__":
    main()
