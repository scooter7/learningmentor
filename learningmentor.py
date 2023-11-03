import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

def ask_openai(messages):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    return response.choices[0].message['content'].strip()

st.title('Leadership Mentor App')

with st.form(key='leadership_form'):
    user_input = st.text_area("Enter your leadership-related query or request:")
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    if user_input.lower().strip() in ["create leadership growth plan", "mentorship", "coaching conversation examples", "leadership resources"]:
        st.session_state['messages'].append({"role": "system", "content": "You are a Leadership Coach."})
        
    user_message = {"role": "user", "content": user_input}
    st.session_state['messages'].append(user_message)
    
    advice = ask_openai(st.session_state['messages'])
    st.session_state['messages'].append({"role": "assistant", "content": advice})
    
    for message in st.session_state['messages']:
        if message['role'] == 'user':
            st.text_area("You", value=message['content'], disabled=True, key=message['content'])
        elif message['role'] == 'assistant':
            st.text_area("Leadership Mentor", value=message['content'], disabled=True, key=message['content'])
