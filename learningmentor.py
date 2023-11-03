import openai
import streamlit as st

# Use Streamlit's secrets object to load the API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Function to send prompts to the OpenAI API
def ask_openai(prompt_text):
    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt_text,
        max_tokens=500
    )
    return response.choices[0].text.strip()

# Initialize the Streamlit app
st.title('Leadership Mentor App')

# Using a form to get user input
with st.form(key='leadership_form'):
    user_input = st.text_area("Enter your leadership-related query or request:")
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    if user_input.lower().strip() == "create leadership growth plan":
        # If the user wants to create a growth plan, ask a series of questions
        st.header("Leadership Growth Plan")
        goals = st.text_input("What are your main leadership goals?")
        challenges = st.text_input("What challenges are you currently facing?")
        successes = st.text_input("What have been your recent successes?")
        if st.button('Generate Growth Plan'):
            prompt_text = f"|Leadership Mentor:|\nCREATE LEADERSHIP GROWTH PLAN\nGoals: {goals}\nChallenges: {challenges}\nSuccesses: {successes}"
            advice = ask_openai(prompt_text)
            st.write(advice)

    elif user_input.lower().strip() == "mentorship":
        # If the user is seeking mentorship
        st.header("Leadership Mentorship")
        issue = st.text_input("What specific issue would you like to discuss?")
        if st.button('Get Mentorship Advice'):
            prompt_text = f"|Leadership Mentor:|\nMENTORSHIP\nIssue: {issue}"
            advice = ask_openai(prompt_text)
            st.write(advice)

    elif user_input.lower().strip() == "coaching conversation examples":
        # If the user wants examples of coaching conversations
        st.header("Coaching Conversation Examples")
        context = st.text_input("What is the context of the conversation you're looking to have?")
        if st.button('Show Examples'):
            prompt_text = f"|Leadership Mentor:|\nCOACHING CONVERSATION EXAMPLES\nContext: {context}"
            advice = ask_openai(prompt_text)
            st.write(advice)

    elif user_input.lower().strip() == "leadership resources":
        # If the user is looking for resources
        st.header("Leadership Resources")
        topic = st.text_input("What topic do you need resources for?")
        if st.button('Provide Resources'):
            prompt_text = f"|Leadership Mentor:|\nLEADERSHIP RESOURCES\nTopic: {topic}"
            advice = ask_openai(prompt_text)
            st.write(advice)
    else:
        # For any other general leadership advice
        prompt_text = f"|Leadership Mentor:|\n{user_input}"
        advice = ask_openai(prompt_text)
        st.write(advice)
