import streamlit as st
import json
from datetime import date

st.set_page_config(page_title="Avyu DPDP Compliance Checklist", layout="wide")

st.title("Avyu — DPDP Compliance Checklist")
st.caption("Digital Personal Data Protection Act, 2023")

# -----------------------------
# SECTION 1 – ORGANIZATION PROFILE
# -----------------------------
st.header("1️⃣ Organization Profile")

with st.expander("Basic Details", expanded=True):
    col1, col2 = st.columns(2)

    with col1:
        org_name = st.text_input("Legal Name of Organization *")
        cin = st.text_input("CIN / Registration Number *")
        employees = st.text_input("Approx. Employees *")
        website = st.text_input("Website Domain *")

    with col2:
        sector = st.text_input("Industry Sector *")
        turnover = st.text_input("Annual Turnover *")
        locations = st.text_input("Locations *")

st.subheader("DPDP Applicability")

yn_pdp = st.radio("Do you process digital personal data?", ["Yes", "No"])
yn_child = st.radio("Do you process children's data?", ["Yes", "No"])
yn_outside = st.radio("Operate outside India?", ["Yes", "No"])
yn_sdf = st.radio("Likely Significant Data Fiduciary?", ["Yes", "No"])

# -----------------------------
# SECTION 2 – DATA INVENTORY
# -----------------------------
st.header("2️⃣ Data Inventory Checklist")

data_types = st.multiselect(
    "Categories of Data Collected",
    [
        "Name","Phone","Email","Aadhaar","PAN","Financial",
        "Health","Biometric","Employee","Student","Vendor"
    ]
)

sources = st.multiselect(
    "Sources of Data",
    ["Website Forms","Mobile App","Offline Forms",
     "Third-party Integrations","HR Systems","CRM"]
)

storage = st.multiselect(
    "Storage Locations",
    ["On-prem","AWS/Cloud","Google Workspace",
     "SaaS","Excel Files","Email"]
)

# -----------------------------
# SECTION 3 – CONSENT
# -----------------------------
st.header("3️⃣ Consent & Notice")

yn_consent1 = st.radio("Do you collect explicit consent?", ["Yes", "No"])
yn_consent2 = st.radio("Is consent purpose specific?", ["Yes", "No"])
yn_consent3 = st.radio("Is consent recorded?", ["Yes", "No"])
yn_consent4 = st.radio("Can users withdraw consent?", ["Yes", "No"])
yn_consent5 = st.radio("Is withdrawal logged?", ["Yes", "No"])

st.subheader("Privacy Notice")

yn_pn1 = st.radio("Privacy Policy exists?", ["Yes", "No"])
yn_pn2 = st.radio("Updated for DPDP 2023?", ["Yes", "No"])
yn_pn3 = st.radio("Multi-language?", ["Yes", "No"])
yn_pn4 = st.radio("Mentions grievance officer?", ["Yes", "No"])
yn_pn5 = st.radio("Explains retention?", ["Yes", "No"])

# -----------------------------
# SECTION 4 – SECURITY
# -----------------------------
st.header("4️⃣ Security Safeguards")

technical_controls = st.multiselect(
    "Technical Controls",
    ["Encryption at Rest","Encryption in Transit",
     "RBAC","MFA","Log Monitoring","Firewall","Endpoint Security"]
)

org_controls = st.multiselect(
    "Organizational Controls",
    ["InfoSec Policy","Employee NDA",
     "Security Training","Vendor Risk Assessment"]
)

# -----------------------------
# SECTION 5 – BREACH MANAGEMENT
# -----------------------------
st.header("5️⃣ Breach Management")

yn_bm1 = st.radio("Incident Response Policy?", ["Yes", "No"])
yn_bm2 = st.radio("Breach reporting defined?", ["Yes", "No"])
yn_bm3 = st.radio("72-hour workflow established?", ["Yes", "No"])
yn_bm4 = st.radio("Escalation matrix documented?", ["Yes", "No"])
yn_bm5 = st.radio("Breach register maintained?", ["Yes", "No"])

# -----------------------------
# SECTION 6 – DATA PRINCIPAL RIGHTS
# -----------------------------
st.header("6️⃣ Data Principal Rights")

yn_dr1 = st.radio("Access request process?", ["Yes", "No"])
yn_dr2 = st.radio("Correction mechanism?", ["Yes", "No"])
yn_dr3 = st.radio("Erasure process?", ["Yes", "No"])
yn_dr4 = st.radio("Grievance redressal?", ["Yes", "No"])
yn_dr5 = st.radio("Nomination process?", ["Yes", "No"])

# -----------------------------
# SECTION 7 – GOVERNANCE
# -----------------------------
st.header("7️⃣ Governance & Accountability")

yn_gov1 = st.radio("DPO appointed?", ["Yes", "No"])
yn_gov2 = st.radio("DPO in India?", ["Yes", "No"])
yn_gov3 = st.radio("DPIA conducted?", ["Yes", "No"])
yn_gov4 = st.radio("Annual review scheduled?", ["Yes", "No"])
yn_gov5 = st.radio("Audit logs maintained?", ["Yes", "No"])
yn_gov6 = st.radio("Board oversight exists?", ["Yes", "No"])

# -----------------------------
# OBSERVATIONS
# -----------------------------
st.header("📝 Observations")
observations = st.text_area("Additional Notes")

# -----------------------------
# SIGN OFF
# -----------------------------
st.header("✍ Reviewer Sign-Off")

reviewer = st.text_input("Reviewer Name *")
designation = st.text_input("Designation *")
review_date = st.date_input("Date of Review", value=date.today())
signature = st.text_input("Signature")

# -----------------------------
# GENERATE JSON
# -----------------------------
if st.button("Generate Assessment JSON"):

    assessment_data = {
        "orgName": org_name,
        "cin": cin,
        "sector": sector,
        "employees": employees,
        "turnover": turnover,
        "website": website,
        "locations": locations,

        "yn_pdp": yn_pdp,
        "yn_child": yn_child,
        "yn_outside": yn_outside,
        "yn_sdf": yn_sdf,

        "data_types": data_types,
        "sources": sources,
        "storage": storage,

        "yn_consent1": yn_consent1,
        "yn_consent2": yn_consent2,
        "yn_consent3": yn_consent3,
        "yn_consent4": yn_consent4,
        "yn_consent5": yn_consent5,

        "yn_pn1": yn_pn1,
        "yn_pn2": yn_pn2,
        "yn_pn3": yn_pn3,
        "yn_pn4": yn_pn4,
        "yn_pn5": yn_pn5,

        "yn_bm1": yn_bm1,
        "yn_bm2": yn_bm2,
        "yn_bm3": yn_bm3,
        "yn_bm4": yn_bm4,
        "yn_bm5": yn_bm5,

        "yn_dr1": yn_dr1,
        "yn_dr2": yn_dr2,
        "yn_dr3": yn_dr3,
        "yn_dr4": yn_dr4,
        "yn_dr5": yn_dr5,

        "yn_gov1": yn_gov1,
        "yn_gov2": yn_gov2,
        "yn_gov3": yn_gov3,
        "yn_gov4": yn_gov4,
        "yn_gov5": yn_gov5,
        "yn_gov6": yn_gov6,

        "observations": observations,
        "reviewer": reviewer,
        "designation": designation,
        "review_date": str(review_date),
        "signature": signature
    }

    st.success("Assessment Created Successfully")

    st.download_button(
        label="Download JSON",
        data=json.dumps(assessment_data, indent=2),
        file_name="DPDPA_Assessment.json",
        mime="application/json"
    )
