import streamlit as st

from login import login
from dashboard import dashboard


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


if st.session_state.logged_in:

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    dashboard()

else:

    login()
