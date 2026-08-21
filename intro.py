import streamlit as st

def main():
  st.title("Introduction to Streamlit")

  name = st.text_input("Enter your name:")
  st.write(f"Hello,{name}")

if __name__=="__main__":
  main()
