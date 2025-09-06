# 🎓 Smart Course Advisor (Streamlit + ML)

This project is a **Smart Course Advisor** that predicts whether a student is eligible to take the **next course level** based on:
- Quiz Score  
- Time Spent on the course  
- Completion Status  

The app provides **personalized suggestions** and feedback using a trained **Random Forest model**.

---

## ✨ Features
- ✅ Predicts **next course eligibility**  
- ✅ Inputs: `quiz_score`, `time_spent`, `completion_status`  
- ✅ Outputs personalized advice (eligible, revise, improve, etc.)  
- ✅ Simple **Streamlit UI** with sidebar inputs  
- ✅ Trained with **synthetic dataset**  

---

## 🛠 Installation

Clone the repository:
```bash
git clone https://github.com/classytamil/Smart-Course-Advisor.git
cd smart-course-advisor
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

Main dependencies:

* `streamlit`
* `scikit-learn`
* `pandas`
* `numpy`
* `joblib`

Example `requirements.txt`:

```txt
streamlit
scikit-learn
pandas
numpy
joblib
```

---

## 🚀 Usage

Run the app:

```bash
streamlit run app.py
```

---

## 📊 Dataset

The model was trained on a **synthetic dataset** with columns:

* `quiz_score` → student’s quiz score (0–100)
* `time_spent` → total hours spent on the course
* `completion_status` → Completed / Incomplete (binary encoded)
* `next_level` → Target variable (1 = Eligible, 0 = Not Eligible)

---

## 🧠 Model Training

The model used is a **Random Forest Classifier** trained with synthetic student performance data.
It is saved as `model/student_model.pkl` and loaded into the Streamlit app.

---

## 📜 License

This project is licensed under the MIT License. Feel free to use and improve it!
