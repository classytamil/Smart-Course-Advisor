import streamlit as st
import joblib

# Load trained model
model = joblib.load("model/student_model.pkl")

# Page config
st.set_page_config(page_title="Smart Course Advisor", layout="centered")

# Title
st.title("🎓 Smart Course Advisor")
st.markdown("Welcome! Enter student details to check **next course eligibility** and get personalized advice.")

# Sidebar Inputs
st.sidebar.header("📥 Student Input")
student_id = st.sidebar.text_input("Student ID")

course = st.sidebar.selectbox("Select Course", [
    "Relations and Functions",
    "Numbers and Sequences",
    "Algebra",
    "Calculus",
    "Probability",
    "Geometry",
    "Trigonometry",
    "Statistics"
])

quiz_score = st.sidebar.number_input("Quiz Score (0 - 100)", min_value=0, max_value=100, value=50)
time_spent = st.sidebar.number_input("Time Spent (hours)", min_value=1, max_value=200, value=10)
completion_status = st.sidebar.selectbox("Completion Status", ["Incomplete", "Completed"])

# Button
if st.sidebar.button("🔎 Check Eligibility"):
    # Encode completion_status
    status_encoded = 1 if completion_status == "Completed" else 0
    
    # Prepare input
    input_data = [[quiz_score, time_spent, status_encoded]]
    
    # Predict
    prediction = model.predict(input_data)[0]  # 0 = Not eligible, 1 = Eligible
    
    # --- Decision Rules for Suggestions ---
    if prediction == 1:
        if completion_status == "Completed" and quiz_score >= 50 and time_spent <= 100:
            message = "✅ You can take the next course!"
        elif completion_status == "Completed" and time_spent > 100:
            message = "⚠️ You can move on, but you're taking too much time. Try to be faster."
        elif completion_status == "Completed" and quiz_score < 50:
            message = "⚠️ You completed the course, but with a low score. Revise before moving on."
        else:
            message = "👍 You may proceed, but improvement is recommended."
    else:
        if completion_status == "Incomplete":
            message = "❌ You cannot move to the next course. Please complete this course first."
        elif quiz_score < 50:
            message = "❌ Your score is too low. Revise and try again."
        else:
            message = "❌ You cannot move to the next course. Work on your performance."

    # --- Output UI ---
    st.markdown("---")
    st.subheader("📊 Result")
    st.info(f"**Student ID:** {student_id}")
    st.info(f"**Course:** {course}")
    
    # Highlighted suggestion
    if "✅" in message:
        st.success(message)
    elif "⚠️" in message:
        st.warning(message)
    else:
        st.error(message)
