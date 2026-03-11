import streamlit as st
import tempfile
import os
import json

from rule_engine import ComplianceAnalyzer
from report_generator import generate_report

st.set_page_config(page_title="Avyu DPDPA Audit Tool", layout="centered")

st.title("Avyu DPDPA Compliance Dashboard")
st.markdown("Upload Assessment JSON File to Generate Compliance Report")

uploaded_file = st.file_uploader("Upload Assessment JSON", type=["json"])

org_name = st.text_input("Organization Name", value="Client Organization")

if uploaded_file is not None:

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    if st.button("Generate Report"):

        analyzer = ComplianceAnalyzer(temp_path)
        result = analyzer.analyze()

        impacts = []  # can integrate impact engine later
        actions = []  # remediation engine placeholder

        output_file = "DPDPA_Report.pdf"
        generate_report(result, impacts, actions, output_file, org=org_name)

        with open(output_file, "rb") as f:
            st.download_button(
                label="Download Compliance Report",
                data=f,
                file_name="DPDPA_Report.pdf",
                mime="application/pdf"
            )

        st.success("Report Generated Successfully")
