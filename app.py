import streamlit as st
import pandas as pd
import plotly.express as px

from modules.pdf_parser import extract_text_from_pdf
from modules.text_cleaner import clean_text
from modules.ats_score import calculate_ats_score
from modules.recommendations import generate_recommendations
from modules.resume_classifier import classify_resume


st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide"
)


st.title("AI Resume Analyzer")

st.write(
    "Upload resumes and compare candidates using ATS scoring"
)


uploaded_resumes = st.file_uploader(
    "Upload Resumes",
    type=["pdf"],
    accept_multiple_files=True
)


job_description = st.text_area(
    "Paste Job Description"
)


analyze = st.button("Analyze Resumes")


if analyze:

    if uploaded_resumes and job_description:

        results = []

        cleaned_job_description = clean_text(
            job_description
        )

        for resume in uploaded_resumes:

            resume_text = extract_text_from_pdf(
                resume
            )

            cleaned_resume = clean_text(
                resume_text
            )

            score, matched, missing = calculate_ats_score(
                cleaned_resume,
                cleaned_job_description
            )

            recommendations = generate_recommendations(
                score,
                missing
            )

            category = classify_resume(
                cleaned_resume
            )

            results.append({
                "name": resume.name,
                "score": score,
                "matched": matched,
                "missing": missing,
                "recommendations": recommendations,
                "category": category
            })


        results = sorted(
            results,
            key=lambda x: x["score"],
            reverse=True
        )


        st.subheader("Candidate Rankings")

        rank = 1

        for candidate in results:

            st.markdown("---")

            st.header(
                f"#{rank} {candidate['name']}"
            )

            st.subheader("Dashboard")

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "ATS Score",
                f"{candidate['score']}%"
            )

            col2.metric(
                "Matched Skills",
                len(candidate['matched'])
            )

            col3.metric(
                "Missing Skills",
                len(candidate['missing'])
            )


            st.progress(
                int(candidate['score'])
            )


            st.subheader("Predicted Role")

            st.success(
                candidate['category']
            )


            st.subheader("Matched Skills")

            for skill in candidate['matched']:
                st.success(skill)


            st.subheader("Missing Skills")

            for skill in candidate['missing']:
                st.error(skill)


            st.subheader("Recommendations")

            for recommendation in candidate['recommendations']:
                st.warning(recommendation)


            chart_data = pd.DataFrame({
                "Category": ["Matched", "Missing"],
                "Count": [
                    len(candidate['matched']),
                    len(candidate['missing'])
                ]
            })


            fig = px.pie(
                chart_data,
                names="Category",
                values="Count",
                title="Skill Match Analysis"
            )

            st.plotly_chart(fig)

            rank += 1

    else:

        st.warning(
            "Please upload resumes and paste job description"
        )