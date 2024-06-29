import streamlit as st

st.title('My First Streamlist App')

st.write("Welcome to my  streamlt app!")

st.button("Reset", type="primary")
if st.button("Say Hello"): 
  st.write("Why hello there")
else: 
  st.write("Goodbye")
  
  