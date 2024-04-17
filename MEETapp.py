# Function to call OpenAI's GPT model
def ask_gpt(question):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    return response['choices'][0]['message']['content']

# Streamlit app layout
st.title('Meeting Planner for Sales Reps')

# Meeting details input
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
    submit_button = st.form_submit_button("Save Meeting")

if submit_button:
    st.success("Meeting Saved Successfully!")

# AI Question Interface
st.subheader("Ask a Question")
user_question = st.text_input("What do you need help with?")
if st.button("Get Answer"):
    if user_question:
        answer = ask_gpt(user_question)
        st.text_area("Answer", value=answer, height=300)
    else:
        st.error("Please enter a question.")
