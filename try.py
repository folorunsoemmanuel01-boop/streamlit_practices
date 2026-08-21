import streamlit as st

number = st.text_input("Enter num")

st.write(f"Multiplication table for {number}")

for num in range (1,16):
  st.write(f"{number} X {num} = {number * num}
  
