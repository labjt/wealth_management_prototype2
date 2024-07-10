import streamlit as st

st.title("New Wealth Management Prototype")

st.header("Introduction")
st.write("This is a new Streamlit app for further development.")

st.header("User Input")
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")
