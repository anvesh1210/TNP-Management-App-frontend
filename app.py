from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash") #Fatch model
# Function to get a response from the model
def get_response(prompt):
    response = model.generate_content(prompt)
    return response.text

# Streamlit app config
st.set_page_config(page_title="T&P Chatbot", page_icon="🎓")
st.title("🎓 Training & Placement Chatbot 🤖")
st.markdown("Hi! I can help you with queries, profile status, and document assistance.")

# Tabs for different functionalities
tab1, tab2, tab3 = st.tabs(["💬 Query Handling", "📊 Profile Status", "📁 Document Assistant"])

# Session state to store chat history
if 'history' not in st.session_state:
    st.session_state.history = []

# --- Tab 1: Query Handling ---
with tab1:
    st.subheader("Ask your T&P related questions!")
    user_query = st.text_input("Enter your question:")
    if st.button("Submit Query", key="query_btn"):
        if user_query:
            response = get_response(user_query)
            st.session_state.history.append(f"You: {user_query}")
            st.session_state.history.append(f"Bot: {response}")
            st.success("Response:")
            st.write(response)

# --- Tab 2: Profile Status ---
with tab2:
    st.subheader("Check your profile status")
    student_id = st.text_input("Enter your Student ID:")
    if st.button("Check Status"):
        if student_id:
            # Simulated logic (replace with actual DB logic if needed)
            completion = 85  # Assume 85% completed
            pending = ["Upload Resume", "Fill Internship Details"]
            st.success(f"Profile Completion: {completion}%")
            st.info("Pending Tasks:")
            for task in pending:
                st.write(f"🔹 {task}")

# --- Tab 3: Document Assistant ---
with tab3:
    st.subheader("Manage your T&P documents")
    uploaded_file = st.file_uploader("Upload your placement document (PDF/DOCX)", type=["pdf", "docx"])
    if uploaded_file:
        st.success(f"✅ '{uploaded_file.name}' uploaded successfully!")
        st.write("We will review and verify the document shortly.")
    
    view_docs = st.checkbox("Show Uploaded Documents (Simulated)")
    if view_docs:
        # Simulated document list
        st.write("📄 Resume.pdf")
        st.write("📄 Transcript.docx")

# Show full chat history (for query tab)
with st.expander("🗨️ Chat History"):
    for chat in st.session_state.history:
        st.write(chat)
