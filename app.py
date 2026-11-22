import streamlit as st

st.set_page_config(
    page_title="Around The Wooorld",
    layout="centered"
)

st.title("Around The Wooorld")
st.subheader("Geography Quiz")

st.write("Test your knowledge of capitals, flags and population")

quiz_mode = st.selectbox(
    "Choose a category:",
    ["Capitals", "Flags", "Population", "Mixed"]
)

if st.button("Start Quiz"):
    st.success(f"You selected: {quiz_mode}")