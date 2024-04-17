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
    meeting_date = st.date_input("Meeting Date")
    meeting_time = st.time_input("Meeting Time")
    meeting_location = st.text_input("Location")
    meeting_objective = st.text_area("Objective of the Meeting")
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
