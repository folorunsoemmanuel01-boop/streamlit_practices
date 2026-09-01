import streamlit as st

def main():
   st.title("Introduction to Streamlit")

   name = st.text_input("Enter your name:")
   st.write(f"Hello,{name}")

if __name__=="__main__":
   main()



def usersInput():

    st.title("Enter Numbers")

    if "userList" not in st.session_state:
        st.session_state["userList"] = []

    userInput = st.text_input("Enter a number:")

    if st.button("Add Number"):

        if userInput.isdigit():
            st.session_state[userList].append(int(userInput))
            st.success("Number added!")

        elif userInput == "":
            st.warning("Please enter a number")

        else:
            st.error("Invalid Character")

    if st.button("Done"):
        st.write("Your Final List:")
        st.write(st.session_state.userList)


usersInput()

