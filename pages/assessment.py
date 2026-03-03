import streamlit as st
import json

st.title("DPDPA Assessment Form")

consent = st.radio("Do you obtain valid consent?", ["Yes", "No"])
encryption = st.radio("Is data encrypted at rest?", ["Yes", "No"])

if st.button("Download Assessment JSON"):
    data = {
        "yn_consent1": consent,
        "tc_enc_rest": encryption
    }

    st.download_button(
        "Download JSON",
        data=json.dumps(data, indent=2),
        file_name="assessment.json",
        mime="application/json"
    )