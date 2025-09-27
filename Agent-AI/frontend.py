import streamlit as st

st.set_page_config(
  page_title="LangGraph AI Agent",
  page_icon=":robot_face:", 
  layout="centered"
)

st.title("AI Chatbot Agent")
st.write("Create and Interact with LangGraph AI Agent")

system_prompt = st.text_area(
  "Define your AI agent: ",
  height=70, 
  placeholder="Type your system prompt here..."
)

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select Provider:", ("Groq", "OpenAI"))

selected_model: str | None = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ) if provider == "Groq" else st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)

if not selected_model:
    # Handle the case when selected_model is None
    # For example, you can show an error message or set a default value
  st.error("Please select a model.")
  selected_model = "default_model"

allow_web_search = st.checkbox("Allow Web Search", value=True)

user_query = st.text_area(
  "Enter your message: ",
  height=150, 
  placeholder="Ask Anything..."
)

API_URL = "http://localhost:8000/chat"

if st.button("Ask Agent!"):
  if user_query.strip() and selected_model:
    import requests

    payload: dict[str, object] = {  
      "model_name": selected_model,
      "model_provider": provider,
      "system_prompt": system_prompt,
      "messages": [user_query],
      "allow_search": allow_web_search
    }


    response = requests.post(API_URL, json=payload)
    if response.status_code == 200:
      response_data = response.json()
      if "error" in response_data:
        st.error(response_data["error"])
      else:
        st.header("Agent Response:")
        st.markdown(f"**Final Response:** {response_data}")