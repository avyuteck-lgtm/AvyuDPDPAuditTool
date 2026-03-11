import streamlit as st
from auth import authenticate

def login():

    st.title("Avyu DPDP Compliance Audit Tool")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if authenticate(username, password):

            st.session_state.logged_in = True
            st.success("Login successful")
            st.rerun()

        else:
            st.error("Invalid username or password")
