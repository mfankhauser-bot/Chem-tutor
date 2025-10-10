import streamlit as st

# Sample chemistry questions and answers
chemistry_questions = {
    "What is the chemical formula for water?": "H2O",
    "What is the atomic number of carbon?": "6",
    "What is the pH of a neutral solution?": "7",
    "What gas do plants absorb from the atmosphere for photosynthesis?": "Carbon dioxide",
    "What is the main component of table salt?": "Sodium chloride"
}

# Disclosure statement
disclosure = """
**Disclosure Statement**

This chatbot is designed to support Chemistry students by providing formative feedback on their understanding. It compares student responses to expected answers and offers hints or next steps for learning. It is not a substitute for teacher evaluation and includes a human-in-the-loop safeguard for flagged responses. This tool upholds academic integrity by promoting honest self-assessment, fairness by treating all responses equally, and inclusivity by supporting diverse learners with constructive feedback.
"""

# Function to check student answer
def check_answer(question, student_answer):
    correct_answer = chemistry_questions.get(question)
    if not correct_answer:
        return "Question not recognized. Please try another question.", False
    if student_answer.strip().lower() == correct_answer.lower():
        return "✅ Correct! Great job.", True
    else:
        return (
            "❌ That's not quite right. Hint: Think about the basic properties of the substance. "
            "You may want to review this topic and try again.",
            False
        )

# Streamlit app layout
st.title("Chemistry Feedback Chatbot")
st.markdown(disclosure)

st.subheader("Select a Chemistry Question")
selected_question = st.selectbox("Choose a question:", list(chemistry_questions.keys()))

st.subheader("Enter Your Answer")
student_answer = st.text_input("Your answer:")

if st.button("Submit"):
    feedback, is_correct = check_answer(selected_question, student_answer)
    st.write(feedback)

    if not is_correct:
        st.warning("Your response has been flagged for teacher review to ensure accurate feedback and support.")

        # Simulate sending flagged response to teacher
        with open("flagged_responses.txt", "a") as f:
            f.write(f"Question: {selected_question}\nStudent Answer: {student_answer}\n\n")

        st.info("A teacher will review your response and provide additional guidance.")

st.sidebar.title("About This Tool")
st.sidebar.markdown("""
This chatbot helps students practise Chemistry by checking their answers and offering feedback. 
It supports learning through self-assessment and includes teacher oversight for flagged responses.
""")
