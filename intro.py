import streamlit as st

# def main():
#   st.title("Introduction to Streamlit")

#   name = st.text_input("Enter your name:")
#   st.write(f"Hello,{name}")

# if __name__=="__main__":
#   main()

# import random

# def hangman():
#   st.title("Hangman Game")
  
#   words = ["python","game"]
#   word = random.choice(words)

#   guess = st.text_input("Enter a character")
  
#   if guess.isalpha() and len(guess) == 1:
#       st.write(guess)
    
#       if guess in word:
#         st.write(f"The position of the guess is {word.find(guess)}")
#         st.write(f"Yes, The character {guess} is in {word}") 
#       else:
#         st.write("No")
#   else:
#       st.write("Invalid character")

# hangman()

# for i in range(1,11):
#   st.write(f"2 * {i} = {2*i}")


import random
import time

st.title("🎯 Guess the Number Game")

# Initialize game
if "randomNumber" not in st.session_state:
    st.session_state.randomNumber = random.randint(1, 20)

if "attempts" not in st.session_state:
    st.session_state.attempts = 10

if "name" not in st.session_state:
    st.session_state.name = ""

if "score_sheet" not in st.session_state:
    st.session_state.score_sheet = {}

# Get name
if st.session_state.name == "":
    name = st.text_input("Enter your name")

    if st.button("Start Game"):
        if name:
            st.session_state.name = name
            st.rerun()
        else:
            st.warning("Please enter your name")

else:
    st.write(f"Hola, {st.session_state.name} 👋")

    st.write(f"You have {st.session_state.attempts} attempts left")

    # Number input
    guess_number = st.number_input(
        "Enter a number",
        min_value=1,
        max_value=20,
        step=1
    )

    if st.button("Guess"):

        if st.session_state.attempts <= 0:
            st.error("You have no attempts left!")

        elif guess_number > st.session_state.randomNumber:
            st.session_state.attempts -= 1
            st.warning("Too High")

        elif guess_number < st.session_state.randomNumber:
            st.session_state.attempts -= 1
            st.warning("Too Low")

        else:
            st.success(
                f"Congratulations, {st.session_state.name}! "
                f"You got the number 🎉"
            )

            st.session_state.score_sheet[st.session_state.name] = "completed"

            st.write(st.session_state.score_sheet)

            if st.button("Play Again"):
                st.session_state.randomNumber = random.randint(1, 20)
                st.session_state.attempts = 10
                st.rerun()

    # Game over
    if st.session_state.attempts == 0:
        st.error(
            f"Game Over! The number was "
            f"{st.session_state.randomNumber}"
        )

        st.session_state.score_sheet[st.session_state.name] = "completed"

        st.write(st.session_state.score_sheet)

        if st.button("Play Again"):
            st.session_state.randomNumber = random.randint(1, 20)
            st.session_state.attempts = 10
            st.rerun()
