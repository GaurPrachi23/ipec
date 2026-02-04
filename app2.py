import streamlit as st

st.title("my age and my city")

age = st.number_input("enter your age", 1, 100)
city = st.selectbox("select your city", ["mumbai", "delhi", "chennai"])

if st.button("submit"):
    st.write("hrllo", age, city)