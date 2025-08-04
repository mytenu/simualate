import streamlit as st

st.title("Simulating `input()` in Streamlit")

# Input fields
name = st.text_input("Enter your name:")
age = st.text_input("Enter your age:")

# Submit button
if st.button("Submit"):
    if name and age:
        st.success(f"Login Successful")
    else:
        st.warning("Please fill in both name and age.")
