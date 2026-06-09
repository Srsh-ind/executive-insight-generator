import os
import streamlit as st

from analyzer import analyze_data
from insights import generate_insights
from charts import generate_chart
from ppt_builder import create_ppt


st.set_page_config(page_title="Executive Insight Generator", layout="wide")

st.title("Executive Insight Generator")
st.write("Upload a CSV file to generate AI-powered executive insights and a PowerPoint report.")

os.makedirs("temp", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    file_path = "temp/temp.csv"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("Analyzing data..."):
        metrics = analyze_data(file_path)

    with st.spinner("Generating AI insights..."):
        insights_list, risks_list, recs_list = generate_insights(metrics)

    with st.spinner("Creating chart..."):
        chart = generate_chart(file_path)

    with st.spinner("Building PowerPoint..."):
        ppt = create_ppt(insights_list, risks_list, recs_list, chart)

    st.write("### Metrics")
    st.json(metrics)

    st.write("### AI-Generated Insights")
    for insight in insights_list:
        st.write("-", insight)

    st.write("### Risks")
    for risk in risks_list:
        st.write("-", risk)

    st.write("### Recommendations")
    for rec in recs_list:
        st.write("-", rec)

    st.image(chart, caption="Revenue by Region")

    with open(ppt, "rb") as f:
        st.download_button(
            "Download PPT",
            f,
            file_name="executive_insights.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
        )