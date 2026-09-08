import streamlit as st
import random

def main():
  st.title("Hangman Game")
  words = ["Dog","Fish", "Donkey"]

  if "choice" not in st.session_state:
    st.session_state.choice = random.choice(words)
    st.session_state.guesses = list(len(st.session_state.choice)*"_")
    st.session_state.attempts = 5
  
  user_guess = st.text_input("Enter a character:")
  if len(user_guess) == 1:
    if user_guess in st.session_state.choice:
      pos = st.session_state.choice.find(user_guess)
      st.session_state.guesses[pos] = user_guess

      st.write(" ".join(st.session_state.guesses))
    else:
      st.session_state.attempts -= 1
      st.write(f"You have {st.session_state.attempts} attempts left.")
  else:
    st.write("This is not how to play the game!!")

  if st.button("Play Again!"):

    for key in st.session_state.keys():
      del st.session_state[key]

    st.rerun()

if __name__ == "__main__":
  main()
