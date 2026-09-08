import streamlit as st
import random

def main():
  st.title("Hangman Game")
  words = ["Dog","Fish", "Donkey"]

  if "choice" not in st.session_state:
    st.session_state.choice = random.choice(words)
    st.session_state.guesses = len(choice)*"_"
    st.session_state.attempts = 5

  user_guess = st.text_input("Enter a character:")
  if user_guess is not None and len(user_guess) == 1:
    if user_guess in choice:
      pass
    else:
      st.write(f"You have {attempts - 1} attempts left.")
  else:
    st.error("This is not how to play the game!!")

  if st.button("Play Again!"):

    for key in st.session_state.keys():
      del st.session_state[key]

    st.rerun()

if __name__ == "__main__":
  main()
