# import streamlit as st

# number = st.text_input("Enter num")

# st.write(f"Multiplication table for {number}")

# for num in range (1,16):
#   st.write(f"{number} X {num} = {number * num}

  

import streamlit as st
def usersInput():

    st.title("Enter Numbers")

    if "userList" not in st.session_state:
        st.session_state["userList"] = []

    userInput = st.text_input("Enter a number:")

    if st.button("Add Number"):

        if userInput.isdigit():
            st.session_state["userList"].append(int(userInput))
            st.success("Number added!")

        elif userInput == "":
            st.warning("Please enter a number")

        else:
            st.error("Invalid Character")

    if st.button("Done"):
        st.write("Your Final List:")
        st.write(st.session_state["userList"])


usersInput()
  
