import streamlit as st
import json

from rule_engine import ComplianceAnalyzer
from penalty_engine import explain_business_impact
from remediation_engine import remediation_steps
from report_generator import generate_report


def dashboard():

    st.title("Avyu DPDP Compliance Audit Dashboard")

    # Upload JSON file
    uploaded_file = st.file_uploader(
        "Upload Client Assessment JSON",
        type="json"
    )

    # Run only if file is uploaded
    if uploaded_file is not None:

        data = json.load(uploaded_file)

        with open("temp_assessment.json", "w") as f:
            json.dump(data, f)

        analyzer = ComplianceAnalyzer("temp_assessment.json")

        result = analyzer.analyze()

        impacts = explain_business_impact(result["violations"])
        actions = remediation_steps(result["violations"])

        org_name = analyzer.data.get("orgName", "Client Organization")

        generate_report(
            result,
            impacts,
            actions,
            "DPDPA_Report.pdf",
            org=org_name
        )

        st.success("Report Generated Successfully")

        with open("DPDPA_Report.pdf", "rb") as f:
            st.download_button(
                "Download Report",
                f,
                file_name="DPDPA_Report.pdf"
            )
