import streamlit as st
import pandas as pd

# load dataset
data = pd.read_csv("jobs.csv")

st.title("AI-Powered Job Recommendation System 🚀")
st.write("Enter your skills and get the best matching job roles instantly.")

# user input
user_input = st.text_input("Enter your skills (e.g., Python, SQL, Machine Learning):")

if st.button("Recommend Jobs"):
    skills = [skill.strip().lower() for skill in user_input.split(",")]

    results = []

    for index, row in data.iterrows():
        description = row['Job Description'].lower()

        match_count = 0

        for skill in skills:
            if skill in description:
                match_count += 1

        if match_count > 0:
            results.append((row['Job Title'], match_count))

    results.sort(key=lambda x: x[1], reverse=True)

    if not results:
        st.write("No matching jobs found")
    else:
        st.subheader("Recommended Jobs:")
        for job, score in results:
            st.write(f"{job} (match score: {score})")