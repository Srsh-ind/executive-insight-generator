import streamlit as st

from analyzer import analyze_data
from insights import generate_insights
from charts import generate_chart
from ppt_builder import create_ppt


st.title("Executive Insight Generator")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    with open("temp/temp.csv", "wb") as f:
        f.write(uploaded_file.getbuffer())

    metrics = analyze_data("temp/temp.csv")

    insights, risks, recs = generate_insights(metrics)

    chart = generate_chart("temp/temp.csv")

    ppt = create_ppt(insights, risks, recs, chart)

    st.write("### Metrics")
    st.json(metrics)

    st.write("### Insights")
    for insight in insights:
        st.write("-", insight)

    st.write("### Risks")
    for risk in risks:
        st.write("-", risk)

    st.write("### Recommendations")
    for rec in recs:
        st.write("-", rec)

    with open(ppt, "rb") as f:
        st.download_button(
            "Download PPT",
            f,
            file_name="executive_insights.pptx"
        )