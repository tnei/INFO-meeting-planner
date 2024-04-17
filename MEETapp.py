# Ensure you have set your OPENAI_API_KEY in your environment variables or Streamlit secrets
openai.api_key = st.secrets["sk-proj-4hLzih5ZNo0XM8U6JEVmT3BlbkFJ3sJGiaaEs1XdnFLiwaRT"]

# Function to call OpenAI's GPT model
def ask_gpt(question):
    try:
        response = openai.Completion.create(
            model="text-davinci-004",  # Update to the appropriate model you have access to
            prompt=question,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        st.error(f"An error occurred: {e}")
        return "I am unable to provide an answer at this time."

# Streamlit app layout
st.title('Meeting Planner for Sales Reps')

# Meeting details input section
with st.form("meeting_form"):
    client_name = st.text_input("Client Name")
    completed_by = st.text_input("Completed by:")
    call_date = st.date_input("Call Date")
    internal_participants = st.text_input("Internal Participant(s)")
    client_participants = st.text_input("CLIENT participants")
    agenda = st.text_area("Meeting Agenda", placeholder="List the agenda items here")
    reason_for_meeting = st.text_area("Reason for the meeting", placeholder="Main purpose of the meeting...")
    questions = st.text_area("Top 5 Questions to be Asked", placeholder="Enter questions that are crucial for the meeting...")
    value_creation = st.text_area("Value Creation Ideas", placeholder="Describe the value creation ideas here")
    best_action_commitment = st.text_input("Best Action Commitment", placeholder="Get commitment to a small project")
    minimum_acceptable_action = st.text_input("Minimum Acceptable Action")
    submitted = st.form_submit_button("Save Meeting")

if submitted:
    st.success("Meeting Saved Successfully!")

# AI Question Interface section
st.subheader("Ask a Question")
user_question = st.text_input("What do you need help with?", key="question_input")
if st.button("Get Answer", key="answer_button"):
    if user_question:
        with st.spinner('Getting an answer...'):
            answer = ask_gpt(user_question)
            st.text_area("Answer", value=answer, height=300, key="answer_area")
    else:
        st.error("Please enter a question.")
